def main():
    '''Display menu , get option'''
    MENU = "\n(G)et valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(get_score_result(score))
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()

    print("Goodbye!")


def get_valid_score():
    '''det score and check'''
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score
def get_score_result(score):
    '''Rank the score'''
    if score > 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"
main()
