import time                 # Used to pause execution (sleep)
import os                   # Used to safely build file paths
import pygame               # Handles sound playback (blast effect)

# ==================================================
# AUDIO SYSTEM INITIALIZATION
# ==================================================

# Initialize pygame's audio mixer once at startup
# This prepares the sound system for playing audio files
pygame.mixer.init()

# Set blast sound volume (0.0 = mute, 1.0 = maximum)
pygame.mixer.music.set_volume(1.0)

# ==================================================
# SOUND FILE PATH RESOLUTION
# ==================================================

# Get the directory where this script is located
# This allows the program to find the sound file
# regardless of where Python is executed from
BASE_DIR = os.path.dirname(__file__)

# Build the absolute path to the blast sound file
SOUND_PATH = os.path.join(BASE_DIR, "Blast.wav")

# ==================================================
# COUNTDOWN FUNCTION
# ==================================================
def time_counter(start, end=0):
    """
    Performs a countdown from 'start' to 'end',
    then plays a blast sound with a fade-out effect.
    """

    # Countdown loop (counts backwards using step -1)
    for i in range(start, end - 1, -1):
        print(i)                     # Display current number in console
        time.sleep(1)                 # Pause 1 second between numbers

    # --------------------------------------------------
    # Play blast sound after countdown completes
    # --------------------------------------------------
    if os.path.exists(SOUND_PATH):     # Ensure the sound file exists
        pygame.mixer.music.load(SOUND_PATH)  # Load the sound file
        pygame.mixer.music.play()            # Start playing the sound
        print("Kaboom 💥💣💥!")               # Visual confirmation
    else:
        print("Blast sound file not found!") # Warn user if file missing

    # Allow sound to play briefly before fading out
    time.sleep(1.5)

    # Fade out the sound smoothly over 2 seconds (2000 ms)
    pygame.mixer.music.fadeout(2000)

    # --------------------------------------------------
    # Keep the program running until sound playback ends
    # Prevents program from exiting while sound is playing
    # --------------------------------------------------
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)              # Small sleep to prevent high CPU usage

# ==================================================
# PROGRAM ENTRY POINT
# ==================================================

# Get user input for countdown start value
# Wrapped in try-except to prevent crashing on invalid input
try:
    start = int(input("Enter Timer for Countdown: "))
except ValueError:
    print("Invalid number. Exiting program.")
    exit()

# Simple confirmation step before starting countdown
password = input("Enter password for Confirmation: ")

# Validate password before initiating countdown
if password == "1234":
    print("Countdown Initiated...")            # Notify user
    print(f"Starting countdown from {start}...")  # Show start number
    time_counter(start)                        # Start the countdown
else:
    print("Incorrect password. Countdown aborted.")  # Abort if wrong
