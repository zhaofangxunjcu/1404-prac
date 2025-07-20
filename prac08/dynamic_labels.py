from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

root= Builder.load_file('dynamic_labels.kv')


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["A", "B", "C", "D", "E"]

    def build(self):

        main_layout = root.ids.main

        for name in self.names:
            label = Label(text=name, font_size=24)
            main_layout.add_widget(label)

        return root


if __name__ == '__main__':
    DynamicLabelsApp().run()
