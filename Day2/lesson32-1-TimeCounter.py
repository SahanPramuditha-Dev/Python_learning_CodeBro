import time

def time_counter(end,start=0):
    for i in range(start,end+1):
        print(i)
        time.sleep(1)
    print("Time's up!")

time_counter(5)
time_counter(25,15)
