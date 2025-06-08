"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 5
MAX_LENGTH = 15
IS_SPECIAL_CHARACTER_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    for char in password:
        # TODO: count each kind of character (use str methods like isdigit)
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in SPECIAL_CHARACTERS:
            has_special = True

    # TODO: if any of the 'normal' counts are zero, return False
    if not (has_lower and has_upper and has_digit):
        return False

    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero
    if IS_SPECIAL_CHARACTER_REQUIRED and not has_special:
        return False

    # if we get here (without returning False), then the password must be valid
    return True


main()