s = input("Input: ")
print("Output: ", end="")
for c in s:
    if c.lower() == 'a' or c.lower() == 'e' or c.lower() == 'i' or c.lower() == 'o' or c.lower() == 'u':
        c = ''
    print(c, end="")
