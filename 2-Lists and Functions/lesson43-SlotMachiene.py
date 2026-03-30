import random

# -------------------------------
# CONFIGURATION
# -------------------------------
SYMBOLS = ["🍒", "🍋", "🔔", "⭐", "7️⃣"]
SPIN_COST_MULTIPLIER = 1
JACKPOT_START = 500

# -------------------------------
# GAME STATE
# -------------------------------
balance = 200
jackpot = JACKPOT_START
history = []
 

def spin():
    """Return 3 random slot symbols"""
    return [random.choice(SYMBOLS) for _ in range(3)]


def check_win(result, bet):
    """
    Check winnings based on slot result.
    Returns winnings amount.
    """
    global jackpot

    # JACKPOT CONDITION
    if result == ["7️⃣", "7️⃣", "7️⃣"]:
        win = jackpot * 5   # Jackpot multiplier
        jackpot = JACKPOT_START
        return win

    # ALL THREE MATCH
    if result[0] == result[1] == result[2]:
        jackpot += bet
        return bet * 3

    # TWO MATCH
    if result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
        jackpot += bet
        return bet * 2

    # NO WIN
    jackpot += bet
    return 0


# -------------------------------
# MAIN GAME LOOP
# -------------------------------
print("🎰 Welcome to the Advanced Slot Machine 🎰")

while balance > 0:
    print(f"\nBalance: ${balance}")
    print(f"Jackpot: ${jackpot}")

    bet = input("Enter bet amount (or 'q' to quit): ").lower()

    if bet == "q":
        break

    if not bet.isdigit() or int(bet) <= 0:
        print("❌ Invalid bet amount.")
        continue

    bet = int(bet)

    if bet > balance:
        print("❌ Insufficient balance.")
        continue

    balance -= bet

    result = spin()
    print(" | ".join(result))

    winnings = check_win(result, bet)
    balance += winnings

    # Store play history
    history.append({
        "bet": bet,
        "result": result,
        "winnings": winnings,
        "balance_after": balance
    })

    if winnings > 0:
        print(f"🎉 You won ${winnings}!")
    else:
        print("❌ No win this time.")

print("\n🎮 Game Over")
print(f"Final balance: ${balance}")

# -------------------------------
# SHOW PLAY HISTORY
# -------------------------------
print("\n📜 Play History:")
for i, play in enumerate(history, start=1):
    print(
        f"{i}. Bet: ${play['bet']} | "
        f"Result: {' '.join(play['result'])} | "
        f"Winnings: ${play['winnings']} | "
        f"Balance: ${play['balance_after']}"
    )
