class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

#Used for Strings
    def __str__(self):
        return f"'{self.title}' by {self.author}"

#Used for length
    def __len__(self):
        return self.num_pages
    
#equal Method
    def __eq__(self, other): # other means the other book
        return self.title == other.title or self.author == other.author
    
#find a keyword
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    

#finding Keys
    def __getitem__(self, key):
        key = key.lower()  # normalize input

        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key in ["num_pages", "num pages"]:
            return self.num_pages
        else:
            return f"The searched key '{key}' was not found."

# Creating 3 book objects
book1 = Book("The Last Theorem", "Arthur C. Clarke", 800)
book2 = Book("Atomic Habits", "James Clear", 320)
book3 = Book("Rich Dad Poor Dad", "Robert Kiyosaki", 336)
book4 = Book("3001","Arthur C. Clarke", 400)

print("----------Book Objects-----\n")

print(book1)
print(book2)
print(book3)

print("\n----------Length----------\n")

print(len(book1))
print(len(book2))
print(len(book3))

print("\n----------Equal----------\n")

print("Is Book 1 equal by title or by author to Book 2: ",book1 == book2)
print("Is Book 1 equal by title or by author to Book 4: ",book1 == book4)

print("\n----------Keyword Finding----------\n")

print("Rowling" in book1)
print ("arthur" in book1)
print ("Arthur" in book1)

print("\n----------Key Finding----------\n")
print(book1["author"])
print(book1["audio"])

