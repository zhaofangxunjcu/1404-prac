"""
CP1404/CP5632 - Practical
Fixed program to determine score status
"""
def main():
    score = float(input("Enter score: "))

    get_score_result(score)


def get_score_result(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score > 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()
