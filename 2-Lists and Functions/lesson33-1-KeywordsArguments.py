def get_phone(country,area,first,last):
    return f"+{country} ({area})-{first} {last}"

phone1 = get_phone(country=94,area=11,first=2288,last=573) # By using keyword arguments, we can specify the values for each parameter by name, rather than relying on their position in the function call. This allows us to provide the arguments in any order we like, as long as we specify the parameter names correctly.
print(phone1)