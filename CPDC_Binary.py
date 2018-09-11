for i in range(17):
    print("{0:>1} in binary is {0:>08b}".format(i))
print("-"*20)
for i in range(17):
    print("{0:>1} in binary is {0:>02x}".format(i))

print("-"*20)

fruit = {"apple": "apple-1", "orange": "orange", "lemon": "lemon", "grape": "grape", "apple": "apple-1"}

print(fruit)
print(fruit["apple"])
del fruit["apple"]
print(fruit)
fruit.get()

