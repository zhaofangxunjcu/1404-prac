from pywin32_testutil import non_admin_error_codes

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi
def main():
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
    print("q)uit, c)hoose taxi, d)rive")

def display_taxis(taxis):


def choose_taxi(taxis):
    non_admin_error_codes
def drive_taxi(taxi):
    try:
        return 0

