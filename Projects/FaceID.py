"""
FaceID: Webcam-based face registration and identification.

Features:
- Face Detection
- Face Encoding (feature extraction)
- Face Registration (store encoding + user data)
- Face Matching
- Data Display on successful identification

Install dependencies:
    pip install opencv-python face_recognition numpy

Examples:
    python FaceID.py register --user-id U001 --name "Alice" --email "alice@example.com" --role "Admin"
    python FaceID.py recognize --tolerance 0.45
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path
from typing import Any

_IMPORT_ERROR: ModuleNotFoundError | None = None
try:
    import cv2
    import face_recognition
    import numpy as np
except ModuleNotFoundError as exc:
    _IMPORT_ERROR = exc


DB_FILE = Path("face_db.json")
WINDOW_NAME_CAPTURE = "FaceID - Registration Capture"
WINDOW_NAME_RECOGNIZE = "FaceID - Recognition"
DEFAULT_TOLERANCE = 0.45
UNKNOWN_REPROMPT_DISTANCE = 0.40


def ensure_dependencies() -> None:
    if _IMPORT_ERROR is None:
        return
    missing = _IMPORT_ERROR.name or "required package"
    raise RuntimeError(
        f"Missing dependency '{missing}'. Install with: "
        "pip install opencv-python face_recognition numpy"
    )


def load_database(db_path: Path) -> list[dict[str, Any]]:
    if not db_path.exists():
        return []

    with db_path.open("r", encoding="utf-8") as file:
        data = json.load(file)
        if not isinstance(data, list):
            raise ValueError(f"Database format error in {db_path}")
        return data


def save_database(db_path: Path, records: list[dict[str, Any]]) -> None:
    with db_path.open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=2)


def _record_encoding_lists(record: dict[str, Any]) -> list[list[float]]:
    encodings_field = record.get("encodings")
    parsed: list[list[float]] = []

    if isinstance(encodings_field, list):
        for item in encodings_field:
            if isinstance(item, list) and item:
                parsed.append(item)

    # Backward compatibility with older schema that had one "encoding".
    legacy_encoding = record.get("encoding")
    if isinstance(legacy_encoding, list) and legacy_encoding:
        if not parsed:
            parsed.append(legacy_encoding)

    return parsed


def _set_record_encodings(record: dict[str, Any], encodings: list[list[float]]) -> None:
    record["encodings"] = encodings
    if encodings:
        # Keep first encoding in the legacy field for compatibility with old data readers.
        record["encoding"] = encodings[0]


def _to_numpy_encoding(encoding_list: list[float]) -> np.ndarray:
    return np.array(encoding_list, dtype=np.float64)


def _build_known_face_index(records: list[dict[str, Any]]) -> tuple[list[np.ndarray], list[int]]:
    known_encodings: list[np.ndarray] = []
    owner_indices: list[int] = []
    for idx, record in enumerate(records):
        for enc in _record_encoding_lists(record):
            known_encodings.append(_to_numpy_encoding(enc))
            owner_indices.append(idx)
    return known_encodings, owner_indices


def _is_close_to_any(target: np.ndarray, vectors: list[np.ndarray], threshold: float) -> bool:
    if not vectors:
        return False
    distances = face_recognition.face_distance(vectors, target)
    return float(np.min(distances)) <= threshold


def _prompt_non_empty(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Value cannot be empty.")


def _select_existing_record(records: list[dict[str, Any]]) -> int | None:
    if not records:
        print("No existing users in database.")
        return None

    print("\nExisting users:")
    for idx, record in enumerate(records, start=1):
        sample_count = len(_record_encoding_lists(record))
        print(f"  {idx}. {record.get('name', 'Unknown')} ({record.get('user_id', '')}) - samples: {sample_count}")

    while True:
        choice = input("Select by number or user_id (blank to cancel): ").strip()
        if not choice:
            return None

        if choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(records):
                return index

        choice_lower = choice.lower()
        for idx, record in enumerate(records):
            if str(record.get("user_id", "")).lower() == choice_lower:
                return idx

        print("Invalid selection. Try again.")


def _enroll_unknown_face(unknown_encoding: np.ndarray, records: list[dict[str, Any]]) -> bool:
    print("\nUnknown face detected.")
    print("Choose enrollment option:")
    print("  n = add as NEW person")
    print("  e = add to EXISTING person")
    print("  s = skip")

    while True:
        choice = input("Your choice [n/e/s]: ").strip().lower()
        if choice in {"n", "e", "s"}:
            break
        print("Invalid choice. Enter n, e, or s.")

    if choice == "s":
        print("Skipped enrollment for this face.")
        return False

    if choice == "n":
        while True:
            user_id = _prompt_non_empty("Enter user_id: ")
            if any(str(record.get("user_id", "")) == user_id for record in records):
                print(f"user_id '{user_id}' already exists. Use a different ID.")
                continue
            break

        name = _prompt_non_empty("Enter name: ")
        email = input("Enter email (optional): ").strip()
        role = input("Enter role (optional): ").strip()
        encoding_list = unknown_encoding.tolist()

        new_record = {
            "user_id": user_id,
            "name": name,
            "email": email,
            "role": role,
            "registered_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
            "encodings": [encoding_list],
            "encoding": encoding_list,
        }
        records.append(new_record)
        print(f"Added new user '{name}' ({user_id}).")
        return True

    selected_index = _select_existing_record(records)
    if selected_index is None:
        print("Enrollment canceled.")
        return False

    record = records[selected_index]
    current_encodings = _record_encoding_lists(record)
    current_encodings.append(unknown_encoding.tolist())
    _set_record_encodings(record, current_encodings)
    record["updated_at"] = datetime.utcnow().isoformat(timespec="seconds") + "Z"
    print(
        f"Added new face sample to '{record.get('name', 'Unknown')}' "
        f"({record.get('user_id', '')}). Total samples: {len(current_encodings)}"
    )
    return True


def _draw_face_box(frame: np.ndarray, top: int, right: int, bottom: int, left: int, label: str) -> None:
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
    cv2.rectangle(frame, (left, bottom - 28), (right, bottom), (0, 255, 0), cv2.FILLED)
    cv2.putText(
        frame,
        label,
        (left + 6, bottom - 8),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (0, 0, 0),
        1,
        cv2.LINE_AA,
    )


def _open_camera(index: int = 0) -> cv2.VideoCapture:
    camera = cv2.VideoCapture(index)
    if not camera.isOpened():
        raise RuntimeError("Could not open webcam. Check camera permissions/device index.")
    return camera


def _detect_and_encode(frame: np.ndarray, model: str = "hog") -> tuple[list[tuple[int, int, int, int]], list[np.ndarray]]:
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    locations = face_recognition.face_locations(rgb_frame, model=model)
    encodings = face_recognition.face_encodings(rgb_frame, known_face_locations=locations)
    return locations, encodings


def capture_one_frame() -> np.ndarray | None:
    camera = _open_camera()
    try:
        while True:
            ok, frame = camera.read()
            if not ok:
                continue

            guide = "Press C to capture | Press Q to cancel"
            cv2.putText(frame, guide, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (20, 220, 20), 2, cv2.LINE_AA)
            cv2.imshow(WINDOW_NAME_CAPTURE, frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("c"):
                return frame
            if key == ord("q"):
                return None
    finally:
        camera.release()
        cv2.destroyWindow(WINDOW_NAME_CAPTURE)


def register_user(args: argparse.Namespace) -> None:
    ensure_dependencies()
    records = load_database(DB_FILE)
    existing_idx = next((i for i, r in enumerate(records) if r.get("user_id") == args.user_id), None)

    if existing_idx is not None and not args.overwrite:
        raise ValueError(f"user_id '{args.user_id}' already exists. Use --overwrite to replace it.")

    print("Opening webcam for registration capture...")
    frame = capture_one_frame()
    if frame is None:
        print("Registration cancelled.")
        return

    locations, encodings = _detect_and_encode(frame, model=args.model)

    if len(locations) == 0:
        raise ValueError("No face detected. Try again in better lighting and face the camera.")
    if len(locations) > 1:
        raise ValueError("Multiple faces detected. Keep only one person in frame and try again.")

    record = {
        "user_id": args.user_id,
        "name": args.name,
        "email": args.email,
        "role": args.role,
        "registered_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
        "encodings": [encodings[0].tolist()],
        "encoding": encodings[0].tolist(),
    }

    if existing_idx is None:
        records.append(record)
    else:
        records[existing_idx] = record

    save_database(DB_FILE, records)
    print(f"Registration successful for '{args.name}' ({args.user_id}).")
    print(f"Database path: {DB_FILE.resolve()}")


def _print_user_data(record: dict[str, Any], distance: float) -> None:
    confidence = max(0.0, min(1.0, 1.0 - distance))
    print("\nIDENTIFIED USER")
    print(f"  user_id: {record.get('user_id', '')}")
    print(f"  name: {record.get('name', '')}")
    print(f"  email: {record.get('email', '')}")
    print(f"  role: {record.get('role', '')}")
    print(f"  similarity_score: {confidence:.3f}\n")


def recognize_users(args: argparse.Namespace) -> None:
    ensure_dependencies()
    records = load_database(DB_FILE)
    if not records:
        raise ValueError(f"No registered users found in {DB_FILE}. Register at least one user first.")

    known_encodings, owner_indices = _build_known_face_index(records)

    if not known_encodings:
        raise ValueError("Database has no valid face encodings.")

    print("Starting recognition. Press Q to quit.")
    camera = _open_camera()
    already_announced: set[str] = set()
    prompted_unknowns: list[np.ndarray] = []

    try:
        while True:
            ok, frame = camera.read()
            if not ok:
                continue

            # Resize for speed, then map locations back to original size.
            small = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            locations_small, encodings = _detect_and_encode(small, model=args.model)
            unknown_candidates: list[np.ndarray] = []

            for (top, right, bottom, left), unknown_encoding in zip(locations_small, encodings):
                distances = face_recognition.face_distance(known_encodings, unknown_encoding)
                best_idx = int(np.argmin(distances))
                best_distance = float(distances[best_idx])

                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                if best_distance <= args.tolerance:
                    record = records[owner_indices[best_idx]]
                    uid = str(record.get("user_id", ""))
                    name = str(record.get("name", "Unknown"))
                    role = str(record.get("role", ""))
                    label = f"{name} ({uid})"
                    _draw_face_box(frame, top, right, bottom, left, label)

                    if role:
                        cv2.putText(
                            frame,
                            f"Role: {role}",
                            (left, max(25, top - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6,
                            (0, 255, 255),
                            2,
                            cv2.LINE_AA,
                        )

                    if uid not in already_announced:
                        _print_user_data(record, best_distance)
                        already_announced.add(uid)
                else:
                    _draw_face_box(frame, top, right, bottom, left, "Unknown")
                    unknown_candidates.append(unknown_encoding)

            cv2.putText(
                frame,
                f"Tolerance: {args.tolerance:.2f} (lower = stricter)",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 180, 255),
                2,
                cv2.LINE_AA,
            )
            cv2.putText(
                frame,
                "Q = quit | Unknown faces trigger terminal enrollment prompt",
                (10, 58),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.55,
                (255, 255, 255),
                1,
                cv2.LINE_AA,
            )
            cv2.imshow(WINDOW_NAME_RECOGNIZE, frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break

            if unknown_candidates:
                # Prompt only once for the same unknown face signature in this session.
                candidate = unknown_candidates[0]
                already_prompted = _is_close_to_any(candidate, prompted_unknowns, UNKNOWN_REPROMPT_DISTANCE)
                if not already_prompted:
                    changed = _enroll_unknown_face(candidate, records)
                    prompted_unknowns.append(candidate)
                    if changed:
                        save_database(DB_FILE, records)
                        known_encodings, owner_indices = _build_known_face_index(records)
                        already_announced.clear()
                        print(f"Database updated: {DB_FILE.resolve()}")
    finally:
        camera.release()
        cv2.destroyWindow(WINDOW_NAME_RECOGNIZE)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Face Detection + Encoding + Registration + Matching + Data Display"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    register_parser = subparsers.add_parser("register", help="Register a user's face and metadata")
    register_parser.add_argument("--user-id", required=True, help="Unique user id")
    register_parser.add_argument("--name", required=True, help="Display name")
    register_parser.add_argument("--email", default="", help="Email address")
    register_parser.add_argument("--role", default="", help="Role/title")
    register_parser.add_argument("--overwrite", action="store_true", help="Replace existing user by user-id")
    register_parser.add_argument(
        "--model",
        choices=["hog", "cnn"],
        default="hog",
        help="Face detector backend (hog is faster on CPU)",
    )
    register_parser.set_defaults(func=register_user)

    recognize_parser = subparsers.add_parser("recognize", help="Run live face matching from webcam")
    recognize_parser.add_argument(
        "--tolerance",
        type=float,
        default=DEFAULT_TOLERANCE,
        help="Match threshold. Lower means stricter matching (typical: 0.4-0.6)",
    )
    recognize_parser.add_argument(
        "--model",
        choices=["hog", "cnn"],
        default="hog",
        help="Face detector backend (hog is faster on CPU)",
    )
    recognize_parser.set_defaults(func=recognize_users)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped by user.")
    except Exception as exc:
        print(f"Error: {exc}")
