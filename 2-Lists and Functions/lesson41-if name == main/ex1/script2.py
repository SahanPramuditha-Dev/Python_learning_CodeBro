from script1 import *

def favourite_drink(drink):
    print(f"Your favourite drink is {drink} ")

def main():
    print("This is the main function in script2.")
    favourite_food("Sushi")
    favourite_drink("Coffee")
    print("End of the main function in script2.")


if __name__ == "__main__":
    main()  