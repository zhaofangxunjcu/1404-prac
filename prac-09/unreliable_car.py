import random
from car import Car

class UnreliableCar(Car):
    """Represent a car that may not always drive when asked."""

    def __init__(self, name, fuel, reliability):
        """Initialise an instance value."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car based on its random value."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            print(f"{self.name} can not drive.")
            return 0
