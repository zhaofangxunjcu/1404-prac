from unreliable_car import UnreliableCar

car = UnreliableCar("TestCar", 10, 30)

for i in range(10):
        distance = car.drive(1)
        print(f"Attempt {i + 1}: Tried to drive 1km, actually drove {distance}km")
