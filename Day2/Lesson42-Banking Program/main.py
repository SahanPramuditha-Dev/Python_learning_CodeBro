# Global balance variable
balance = 0
is_running = True


def show_balance():
    print(f"Your current balance is: {balance}")


def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print("Deposit successful.")
    else:
        print("Invalid deposit amount.")


def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if 0 < amount <= balance:
        balance -= amount
        print("Withdrawal successful.")
    else:
        print("Insufficient balance or invalid amount.")


def transfer():
    global balance
    account_number = input("Enter recipient's account number: ")
    amount = float(input("Enter amount to transfer: "))
    if 0 < amount <= balance:
        balance -= amount
        print(f"Transfer successful to account {account_number}.")
    else:
        print("Insufficient balance or invalid amount.")


while is_running:
    print("\nWelcome to the Banking Program!")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Exit")

    choice = input("Please select an option (1-5): ")

    match choice:
        case "1":
            show_balance()
        case "2":
            deposit()
            show_balance()
        case "3":
            withdraw()
            show_balance()
        case "4":
            transfer()
            show_balance()
        case "5":
            print("Thank you for using the Banking Program. Goodbye!")
            is_running = False
        case _:
            print("Invalid choice. Please select a valid option (1-5).")
