from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi
def main():
    """
       Run the taxi program;Allows the user to choose taxis, drive a selected taxi for a specified distance,
       and track the cumulative bill until quitting."""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0.0
    current_taxi = None
    print("Let's drive!")
    display_menu()
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'c':
            taxi = choose_taxi(taxis)
            if taxi:
                current_taxi = taxi
                current_taxi.start_fare()
            print(f"Bill to date: ${bill:.2f}")
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
                print(f"Bill to date: ${bill:.2f}")
            else:
                bill += drive_taxi(current_taxi)
                print(f"Bill to date: ${bill:.2f}")
        else:
            print("Invalid option")
            print(f"Bill to date: ${bill:.2f}")
        display_menu()
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
def display_menu():
    """Show the menu"""
    print("q)uit, c)hoose taxi, d)rive")
def display_taxis(taxis):
    """List all the taxis."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
def choose_taxi(taxis):
    """Prompt the user to select a taxi from the list."""
    display_taxis(taxis)
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid taxi choice")
        return None
def drive_taxi(taxi):
    """
        Prompt for distance to drive, perform the drive, and report cost
    """
    try:
        distance = float(input("Drive how far? "))
        distance_driven = taxi.drive(distance)
        cost = taxi.get_fare()
        print(f"Your {taxi.name} trip cost you ${cost:.2f}")
        return cost
    except ValueError:
        print("Invalid distance")
        return 0

if __name__ == "__main__":
    main()
