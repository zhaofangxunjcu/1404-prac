import csv
from guitar import Guitar
def main():
    # guitars = load_guitars("guitars.csv")
    # print("These are the guitars we have:")
    # for guitar in guitars:
    #     print(guitar)
    guitars = load_guitars("guitars.csv")
    guitars.sort()
    for g in guitars:
        print(g)


def load_guitars(filename):
    """read csv"""
    guitars = []
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for name, year, cost in reader:
            guitars.append(Guitar(name.strip(), int(year), float(cost)))
    return guitars





if __name__ == "__main__":
    main()
