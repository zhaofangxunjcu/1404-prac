MIN_LENGTH = 6

password = input("Enter a password (at least {} characters): ".format(MIN_LENGTH))

while len(password) < MIN_LENGTH:
    print("Password is too short. Please try again.")
    password = input("Enter a password (at least {} characters): ".format(MIN_LENGTH))

print("*" * len(password))
