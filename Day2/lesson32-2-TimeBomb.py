import time # We need to import the time module to use the sleep function, which allows us to create a delay between each print statement in the countdown.

"""
def time_counter(start,end=0):
    for i in range(start,end-1): 
        print(i)
        time.sleep(1)
    print("Time's up!")

time_counter(5,0)

#this will not work,it will only print as Time's Up because range function counts forward, but we want to count backwards from 5 to 0. To make it count backwards, we need to provide a negative step value in the range function.

"""


def time_counter(start,end=0):
    for i in range(start,end-1,-1): # We use 'end - 1' because range is exclusive of the stop value.
                                    #normmally range function counts forward, but by providing a negative step (-1), we can make it count backwards.
                                    # The '-1' step tells Python to decrement the value of 'i' by 1 in each iteration, allowing us to count downwards from 'start' to 'end'.
        print(i)
        time.sleep(1)
    print("Kaboom 💥💣💥!")

start = int(input("Enter Timer for Countdown: "))
password = input("Enter password for Confirmation: ")
if password == "1234":
    print("Countdown Initiated...")
    print(f"Starting countdown from {start}...")
    time_counter(start)
else:
    print("Incorrect password. Countdown aborted.")