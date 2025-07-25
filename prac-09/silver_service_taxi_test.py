from silver_service_taxi import SilverServiceTaxi



taxi = SilverServiceTaxi("Test Taxi", fuel=100, fanciness=2)
taxi.start_fare()
taxi.drive(18)
fare = taxi.get_fare()
print(taxi)
print(f"Fare for 18 km: ${fare:.2f}")




