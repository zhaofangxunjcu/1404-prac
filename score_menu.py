
def main():
    score = get_valid_score()

    MENU = "\n(G)et valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()

    print("Goodbye!")


def get_valid_score():
    """Get valid score between 0 and 100 (inclusive)."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score


main()
