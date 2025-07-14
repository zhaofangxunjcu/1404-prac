# guitar_collection.py

from guitar import Guitar

guitars = []

print("My guitars!")
name = input("Name: ")
while name :

    year = int(input("Year: "))
    cost = float(input("Cost: "))

    g = Guitar(name, year, cost)
    guitars.append(g)
    print(f"{g} added.\n")
    name = input("Name: ")

print("These are my guitars:")

for i, g in enumerate(guitars, start=1):
    vintage_tag = " (vintage)" if g.is_vintage() else ""
    print(f"Guitar {i}:  {g.name} ({g.year}), worth ${g.cost:,.2f}{vintage_tag}")
