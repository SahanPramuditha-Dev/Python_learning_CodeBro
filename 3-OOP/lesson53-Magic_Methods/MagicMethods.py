#Magic methods (double underscore) __init__ , __str__ , __sq__
            #Automatically called by many of pythons built in operations
            # Allow developers to define or customise the behaviour of objects



class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

# Creating 3 book objects
book1 = Book("The Last Theorem", "Arthur C. Clarke", 300)
book2 = Book("Atomic Habits", "James Clear", 320)
book3 = Book("Rich Dad Poor Dad", "Robert Kiyosaki", 336)

# Using them
print(book1)
print(book2)
print(book3)

#if we print the above it will give these memory addresses
#<__main__.Book object at 0x00000209899186E0>
#<__main__.Book object at 0x0000020989920550>
#<__main__.Book object at 0x0000020989920690>
        