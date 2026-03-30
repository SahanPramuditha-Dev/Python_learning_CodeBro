import datetime

# ---------------- Date Objects ----------------
# Create a specific date (Year, Month, Day)
date = datetime.date(2025, 1, 2)

# Get today's date (system date)
today = datetime.date.today()

# ---------------- Time Object ----------------
# Create a specific time (Hour, Minute, Second)
time = datetime.time(12, 30, 0)

# ---------------- Datetime Object ----------------
# Get current date and time
now = datetime.datetime.now()

# ---------------- Formatting ----------------
# strftime = "string format time"
# %H -> Hour (24h)
# %M -> Minute
# %S -> Second
# %d -> Day
# %m -> Month
# %y -> 2-digit Year
# %Y -> 4-digit Year

now_frmt1 = now.strftime("%H : %M : %S , %d - %m - %y")
now_frmt2 = now.strftime("%H : %M : %S , %d - %m - %Y")
now_frmt3 = now.strftime("%H : %M : %S , %d")

# ---------------- Output ----------------
print(date)         # Specific date
print(today)        # Today's date
print(time)         # Fixed time
print(now)          # Full current datetime
print(now_frmt1)    # Custom format (short year)
print(now_frmt2)    # Custom format (full year)
print(now_frmt3)    # Partial format

target_datetime = datetime.datetime(2030,1,2,12,30,1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date Has PASSED ❌ ")
else:
    print("Target date Has NOT PASSED ✅ ")
