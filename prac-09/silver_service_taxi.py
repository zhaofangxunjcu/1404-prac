from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised Taxi with fanciness multiplier and flagfall fee."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return the total fare, rounded to nearest 10c (includes flagfall)."""
        total_fare = super().get_fare() + self.flagfall
        return round(total_fare * 10) / 10

    def __str__(self):
        return f"{super().__str__()}, ${self.price_per_km:.2f}/km plus flagfall of ${self.flagfall:.2f}"
