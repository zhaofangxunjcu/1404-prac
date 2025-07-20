from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
class Covertmileskm(App):
    message = StringProperty()
    def build(self):
        """Construct the app."""
        self.title = "Convert miles to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = ""
        return self.root
    def convert(self):
        try:
            miles = float(self.root.ids.input_miles.text)
            km = miles * 1.60934
            self.root.ids.output_km.text = f'{km:.5f}'
        except ValueError:
            self.root.ids.output_km.text = '0.0'

    def increase(self):
        try:
            value = float(self.root.ids.input_miles.text)
        except ValueError:
            value = 0
        value += 1
        self.root.ids.input_miles.text = str(int(value))

    def decrease(self):
        try:
            value = float(self.root.ids.input_miles.text)
        except ValueError:
            value = 0
        value -= 1
        self.root.ids.input_miles.text = str(int(value))

Covertmileskm().run()