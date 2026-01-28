#Local Operators = or , and , not

temp = float(input("Enter the temperature: "))
is_raining = False

if temp > 20 and is_raining == False:
    weather_condition = "Sunny"
else:
    weather_condition = "Rainy"

if temp > 35:
    feel = "Hot"
elif temp > 25:
    feel = "Warm"
elif temp > 15:
    feel = "Normal Temperature"
elif temp > 0:
    feel = "Cool"
else:
    feel = "Cold"

if temp > 35 or temp < 0 or is_raining :
    print(f"Outdoor Event is cancelled Because it is {feel} outside and it is {weather_condition}. Sorry for the Inconvenience.")
else:
    print(f"Outdoor Event Will be held on time as it is  {feel} outside and it is {weather_condition} ")

"""
#Improved Code

# Weather & Event Checker

# Get temperature from user
temp = float(input("Enter the temperature (°C): "))

# Ask if it is raining
is_raining_input = input("Is it raining? (yes/no): ").strip().lower()
is_raining = is_raining_input in ["yes", "y"]

# Determine weather condition
if temp > 20 and not is_raining:
    weather_condition = "Sunny"
else:
    weather_condition = "Rainy"

# Determine how the temperature feels
if temp > 35:
    feel = "Hot"
elif temp > 25:
    feel = "Warm"
elif temp > 15:
    feel = "Normal Temperature"
elif temp > 0:
    feel = "Cool"
else:
    feel = "Cold"

# Determine event status
if temp > 35 or temp < 0 or is_raining:
    event_status = "cancelled"
else:
    event_status = "held on time"

# Output final result
print(f"\nOutdoor Event is {event_status} because it is {feel} outside and the weather is {weather_condition}.")



"""