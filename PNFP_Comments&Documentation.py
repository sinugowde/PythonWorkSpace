def greet(name, greeting="Hello"):
    """Print a greeting to the user `name`
    Optional parameter `greeting` can change what they're greeted with."""
    print("{} {}".format(greeting, name))

help(greet)

print("-" * 40)
greet('Shrinivas')
print("-" * 40)
greet('Shrinivas', greeting='Good Day')


