x, y, z = input("Expression: ").split(" ")
if y =='+':
    a = float(x) + float(z)
if y =='-':
    a = float(x) - float(z)
if y =='*':
    a = float(x) * float(z)
if y =='/':
    a = float(x) / float(z)
print(f"{a:.1f}")
