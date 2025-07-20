"""Demo Kivy app adding dynamic labels to a layout."""
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

root= Builder.load_file('dynamic_labels.kv')


class DynamicLabelsApp(App):
    """App that adds labels dynamically based on a list of names."""
    def __init__(self, **kwargs):
        """Initialize with default names."""
        super().__init__(**kwargs)
        self.names = ["A", "B", "C", "D", "E"]

    def build(self):
        """Build UI by creating and adding labels for each name."""
        main_layout = root.ids.main

        for name in self.names:
            label = Label(text=name, font_size=24)
            main_layout.add_widget(label)

        return root


if __name__ == '__main__':
    DynamicLabelsApp().run()
