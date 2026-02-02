import time

"""
my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1): #in revers from the entered seconds to one 
    print(x)
    time.sleep(1) #stop the program for 1 seconds. then to next iterate

print("Time's up!")
"""

"""
#Example 1 Time Hour Seocnd Counter
# Ask the user to enter a number of seconds and convert it to an integer
my_time = int(input("Enter the time in seconds: "))

# Loop starts from the entered time and counts DOWN to 1
# range(start, stop, step)
# start = my_time
# stop = 0 (not included)
# step = -1 (counting backwards)
for x in range(my_time, 0, -1):

    # Get remaining seconds after dividing by 60
    seconds = x % 60  

    # Convert total seconds into minutes, then get remaining minutes after hours are removed
    minutes = (x // 60) % 60  

    # Convert total seconds into hours
    hours = x // 3600  

    # Print the time in HH:MM:SS format
    # :02 means always show 2 digits (adds leading zero if needed)
    # end="\r" keeps printing on the SAME LINE (carriage return)
    print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r")

    # Pause the program for 1 second before next loop iteration
    time.sleep(1)

# This runs after the countdown loop finishes
print("Time's up. Have A Blast 💥💣💥!")

"""

#Example 2 
import sys

my_time = int(input("Enter the time in seconds: "))

# Countdown loop
for x in range(my_time, 0, -1):  # Counts backward from entered seconds to 1
    seconds = x % 60
    minutes = (x // 60) % 60
    hours = x // 3600

    # Display time in HH:MM:SS format on the same line
    print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r")
    time.sleep(1)

# Message to display after countdown
message = "Time's up. Have A Blast 💥💣💥!"

print()  # Move to a new line after countdown finishes

# Print message one character at a time
for letter in message:
    print(letter, end="")
    sys.stdout.flush()   # Forces immediate display
    time.sleep(0.1)      # Wait 0.1 a second between each letter

print()  # Final newline
