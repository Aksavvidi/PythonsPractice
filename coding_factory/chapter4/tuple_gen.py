# generator
generator = (x**2 for x in range(1, 6))

print(type(generator))

for item in generator:
    print(item, end=" ") # 1 4 9 16 25 