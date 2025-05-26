a = str(input("Greeting: ")).strip().lower()
if 'hello' in a.lower():
    print("$0")
elif a.startswith('h'):
    print("$20")
else:
    print("$100")
