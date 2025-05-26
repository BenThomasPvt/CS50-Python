s = input("camelCase: ")
# print("snake_case: ", end="")
for c in s:
    if c.isupper():
        c = '_' + c.lower()
    print(c, end="")
