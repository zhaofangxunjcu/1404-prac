"""
CP1404/CP5632 - Practical
Fixed program to determine score status
"""
import random

def main():
    score = float(input("Enter score: "))
    result = get_score_result(score)
    print(result)
    random_score = random.uniform(0, 100)
    print(f"Random score: {random_score:.2f}")
    print(get_score_result(random_score))

def get_score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()

