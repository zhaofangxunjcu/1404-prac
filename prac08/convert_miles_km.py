from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('convert_miles_km.kv')


class ConverterLayout(BoxLayout):
    def convert(self):
        try:
            miles = float(self.ids.input_miles.text)
            km = miles * 1.60934
            self.ids.output_km.text = f'{km:.5f}'
        except ValueError:
            self.ids.output_km.text = 'Invalid input'

    def increase(self):
        try:
            value = float(self.ids.input_miles.text)
        except ValueError:
            value = 0
        value += 1
        self.ids.input_miles.text = str(int(value))

    def decrease(self):
        try:
            value = float(self.ids.input_miles.text)
        except ValueError:
            value = 0
        value -= 1
        self.ids.input_miles.text = str(int(value))


class MilesToKmApp(App):
    def build(self):
        return ConverterLayout()


if __name__ == '__main__':
    MilesToKmApp().run()
