# Membership Operators in Python are used to check if a value is present in a sequence (like a string, list, tuple, set, or dictionary). The two main membership operators are `in` and `not in`.
# The `in` operator returns `True` if the specified value is found in the sequence, while the `not in` operator returns `True` if the specified value is not found in the sequence.
# Here are some examples to illustrate how these operators work:


word = "Ironman"

letter = input("Enter a letter to check if it is in the Secret Word (Hint :The Marvel Universe depend on Him ): ")

if letter in word:
    print(f"Yes, '{letter}' is in the Secret Word!")
else:
    print(f"No, '{letter}' is not in the Secret Word.")

"""
or else we can use the not in operator to check if a letter is not in the word.

if letter not in word:
    print(f"No, '{letter}' is not in the Secret Word.")
else:
    print(f"Yes, '{letter}' is in the Secret Word!")


"""


characters = { "Sung Jin Woo" , "Naruto Uzumaki" , "Monkey D. Luffy" , "Goku" , "Saitama" , "Deku" , "Tanjiro Kamado" , "Eren Yeager" , "Levi Ackerman" , "Itadori Yuuji" }

character = input("Enter a character to check if it is in the list of popular anime characters: ")

character = character.strip().title()


if character in characters:
    print(f"Yes, '{character}' is in the list of popular anime characters!")

else:
    print(f"No, '{character}' is not in the list of popular anime characters.")

grades = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}

name = input("Enter a name to check if it is in the grades dictionary: ")
name = name.strip().title()

if name in grades:
    print(f"Yes, '{name}' is in the grades dictionary with a grade of {grades[name]}!") #grades[name] is used to access the value associated with the key 'name' in the grades dictionary, which is the grade of the student.
else:
    print(f"No, '{name}' is not in the grades dictionary.")

print("\n-----------------------------\n")


email = input("Enter an email address to check if it is valid (Hint: It should contain '@' and '.'): ")

if "@" in email and "." in email:
    print("Yes, the email address is valid!")
else:
    print("No, the email address is not valid. It should contain '@' and '.'.")

    

