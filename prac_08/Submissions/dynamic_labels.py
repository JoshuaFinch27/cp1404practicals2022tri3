"""
Cp1404 Prac 8 - Dynamically created labels
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program of kivy ap to create dynamic labels"""

    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)
        self.names = ["Joshua Finch", "Jack Francis", "Jacob Brown", "Cat Cyan"]

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Dynamic Labels App"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Creates labels from list entries and adds them to the GUI"""
        for name in self.names:
            temp_label = Label(text=name)
            if __name__ == '__main__':
                self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()