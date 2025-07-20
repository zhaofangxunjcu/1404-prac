from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

# 1) Constant for conversion factor
MILES_TO_KM = 1.60934

class ConvertMilesKm(App):
    message = StringProperty()

    def build(self):
        self.title = "Convert miles to km"
        return Builder.load_file('convert_miles_km.kv')

    def convert(self):
        """Read input, compute km, update label (0.0 on invalid)."""
        try:
            miles = float(self.root.ids.input_miles.text)
            km = miles * MILES_TO_KM
            self.root.ids.output_km.text = f'{km:.5f}'
        except ValueError:
            self.root.ids.output_km.text = '0.0'

    def increase(self):
        """Add 1 to current miles (or start at 0), then convert."""
        try:
            value = float(self.root.ids.input_miles.text)
        except ValueError:
            value = 0
        value += 1
        self.root.ids.input_miles.text = str(int(value))
        self.convert()

    def decrease(self):
        """Subtract 1 from current miles (or start at 0), then convert."""
        try:
            value = float(self.root.ids.input_miles.text)
        except ValueError:
            value = 0
        value -= 1
        self.root.ids.input_miles.text = str(int(value))
        self.convert()

if __name__ == '__main__':
    ConvertMilesKm().run()
