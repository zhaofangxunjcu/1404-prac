"""Demo Kivy BoxLayout app."""
from kivy.app import App
from kivy.lang import Builder



class BoxLayoutDemo(App):
    """Demo app with greet and clear buttons."""
    def build(self):
        """Load UI from KV file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root
    def handle_greet(self):
        """Update label with greeting."""
        print("greet")
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        """Clear input and output."""
        print("clear")
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""

BoxLayoutDemo().run()
