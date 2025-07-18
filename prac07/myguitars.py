import csv
from guitar import Guitar
def main():
    guitars = load_guitars("guitars.csv")
    print("\nExisting guitars:")
    for g in guitars:
        print(" ", g)

    # 2. Let user add new guitars
    added = add_user_guitars()
    if added:
        guitars.extend(added)

        # 3. Save updated list back to file
        save_guitars("guitars.csv", guitars)
        print(f"\nSaved {len(added)} new guitar(s) to {"guitars.csv"}.")

    # 4. Reload and display to verify
    print("\nVerifying all guitars in file:")
    all_guitars = load_guitars("guitars.csv")
    all_guitars.sort()
    for g in all_guitars:
        print(" ", g)
    # print("These are the guitars we have:")
    # for guitar in guitars:
    #     print(guitar)
    # guitars.sort()
    # for g in guitars:
    #     print(g)


def load_guitars(filename):
    """read csv"""
    guitars = []
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for name, year, cost in reader:
            guitars.append(Guitar(name.strip(), int(year), float(cost)))
    return guitars
def save_guitars(filename, guitars):
    """Write a list of Guitar objects to a CSV file."""
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for g in guitars:
            writer.writerow([g.name, g.year, g.cost])

def add_user_guitars():
    """
    Prompt the user to enter new guitars.
    Enter 'done' as the name to finish.
    Returns a list of new Guitar objects.
    """
    new_guitars = []
    print("Enter new guitars (type 'done' as the name to finish):")
    name = input("  Name: ").strip()
    while name!= '':

        if name.lower() == 'done':
            break
        year = int(input("  Year: ").strip())
        cost = float(input("  Cost: ").strip())
        new_guitars.append(Guitar(name, year, cost))
        name = input("  Name: ").strip()
    return new_guitars



if __name__ == "__main__":
    main()
