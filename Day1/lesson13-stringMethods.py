name = "sahAn praMudItha"
phone_Number = "076-4156780"

#get character Count
length = len(name)
print(f"Character Count :{length}") #Space is also count as a character
#Output :- Character Count : 16

#Gives the number of first occurance of the given character
f1 =name.find("h")
print(f"Index of h: {f1}") # When Finding a character it is Case Sensitive
#Output :- Index of h: 2

f2 =name.find("H") #
print(f"Index of H: {f2}") # as H is not avaliable it os given as -1
#Output :- Index of H: -1

#Gives the number of first occurance of the given character from reverse
reverse_Count=name.rfind("t")
print(f"Index of t from reverse count :{reverse_Count}") #this will give the character index from reverse
#Output :- Index of t from reverse count : 11

capitalize = name.capitalize()
print(f"When the name is Capitalized: {capitalize}")
#Output :- When the name is Capitalized: Sahan pramuditha

uppercase = name.upper()
print(f"When the name is Uppercase: {uppercase}")
#Output :- When the name is Uppercase: SAHAN PRAMUDITHA

lowercase = name.lower()
print(f"When the name is Lowercase: {lowercase}")
#Output :- When the name is Lowercase: sahan pramuditha

titlecase = name.title()
print(f"When the name is Titlecase: {titlecase}")
#Output :- When the name is Titlecase: Sahan Pramuditha

isdigit = name.isdigit()
print(f"To check Weather it Include Digits : {isdigit}")
#Output :- To check Weather it Include Digits : False

isspace = name.isspace()
print(f"To check Weather it Include Spaces : {isspace}")
#True if the entire string consists of whitespace characters only (spaces, tabs, newlines)

isalpha = name.isalpha()
print(f"To check Weather it Include Alphabets : {isalpha}")
#Output :- To check Weather it Include Alphabets : False

isnumeric = name.isnumeric()
print(f"To check Weather it is Numeric : {isnumeric}")

isdecimal = name.isdecimal()
print(f"To check Weather it is Decimal : {isdecimal}")

isupper = name.isupper()
print(f"To check Weather it is Uppercase : {isupper}")

islower = name.islower()
print(f"To check Weather it is Lowercase : {islower}")

istitle = name.istitle()
print(f"To check Weather it is Titlecase : {istitle}")

isprintable = name.isprintable()
print(f"To check Weather it is Printable : {isprintable}")

isidentifier = name.isidentifier()
print(f"To check Weather it is Identifier : {isidentifier}")

count_ = phone_Number.count("-")
print(f"Count the Number of '-' : {count_}")

count_2 = phone_Number.count("6")
print(f"Count the Number of '6' : {count_2}")

phone_Number = phone_Number.replace("-"," ") 
print("Phone number after replacing '-' with ' ': ",phone_Number)
#this will replace - with a space 