#keyword Arguments - An argument Precedented by an identifier
                    # When we use keyword arguments in a function call, the order of the arguments does not matter.
                     
def hello(greeting, title, first_name, last_name):
    print(f"{greeting} {title} {first_name} {last_name}")

hello("Hello","Mr.","Lucifer","Morningstar") # Positional arguments
hello("Hi","Strange","Stephen","Mr.")  # We have changed the order of arguments here . So the output will be different Meaningless
hello(first_name="Lucifer", last_name="Morningstar", title="Mr.", greeting="Hello") #  # so we use Keyword arguments, so even if we change the order of arguments, the output will be correct
hello("Good Morning", last_name="Wayne", first_name="Bruce", title="Mr.") # We can also mix positional and keyword arguments, but positional arguments must come before keyword arguments.
# hello("Greetings",title = "Mr.", "Banner", first_name="Bruce") is incorrect because positional argument comes after keyword argument