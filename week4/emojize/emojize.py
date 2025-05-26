import emoji

e = input("Input: ")

eo = emoji.emojize(e, language='alias')

print("Output:", eo)
