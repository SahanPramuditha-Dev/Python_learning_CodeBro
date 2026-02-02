principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle amount must be greater than zero.")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate must be greater than zero.")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time must be greater than zero.")

total = principle * (1 + rate / 100) ** time
print(f"Total amount after {time} years for a principle of ${principle} at an interest rate of {rate}%: ${total:.2f}")