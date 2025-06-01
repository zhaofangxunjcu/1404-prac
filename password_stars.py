def main():
    MIN_LENGTH = 6

    password = get_password(MIN_LENGTH)

    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password(MIN_LENGTH):
    password = input("Enter a password (at least {} characters): ".format(MIN_LENGTH))
    while len(password) < MIN_LENGTH:
        print("Password is too short. Please try again.")
        password = input("Enter a password (at least {} characters): ".format(MIN_LENGTH))
    return password


main()

