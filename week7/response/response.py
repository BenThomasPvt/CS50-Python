import validators

# Prompt the user for an email address
email = input("What's your email address? ")

# Validate the email using the validators library
if validators.email(email):
    print("Valid")
else:
    print("Invalid")
