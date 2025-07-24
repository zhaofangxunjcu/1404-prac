from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised Taxi with fanciness multiplier and flagfall fee."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return full fare ."""
        return round(super().get_fare() + self.flagfall, 2)

    def __str__(self):
        return f"{super().__str__()}, ${self.price_per_km:.2f}/km plus flagfall of ${self.flagfall:.2f}"
