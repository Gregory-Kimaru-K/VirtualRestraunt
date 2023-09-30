from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.filechooser import FileChooserIconView
from kivy.graphics import Color, Rectangle

class LandingPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        # Background color
        self.canvas.before.clear()
        with self.canvas.before:
            Color(1, 0, 0, 1)  # Red background
            Rectangle(pos=self.pos, size=self.size)

        # Title label
        title_label = Label(
            text="B2B Restaurant",
            font_size=30,
            size_hint=(None, None),
            size=(400, 50),
            pos_hint={'center_x': 0.5}
        )

        # Description label
        desc_label = Label(
            text="Order your favorite dishes with ease!",
            font_size=18,
            size_hint=(None, None),
            size=(400, 50),
            pos_hint={'center_x': 0.5}
        )

        # Image insertion button
        image_button = Button(
            text="Insert Picture",
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={'center_x': 0.5}
        )
        image_button.bind(on_press=self.show_file_chooser)

        # Square with circular edges
        square_with_image = BoxLayout(
            orientation='vertical',
            size_hint=(None, None),
            size=(200, 200),
            pos_hint={'center_x': 0.5}
        )

        square_image = Image(
            source="default_image.png",  # Default image path
            size_hint=(None, None),
            size=(200, 200),
            allow_stretch=True,
            keep_ratio=True
        )

        square_with_image.add_widget(square_image)

        self.add_widget(title_label)
        self.add_widget(desc_label)
        self.add_widget(image_button)
        self.add_widget(square_with_image)

    def show_file_chooser(self, instance):
        # Add code here to open a file chooser and set the selected image as the square's image
        pass

class B2BRestaurantApp(App):
    def build(self):
        return LandingPage()

if __name__ == '__main__':
    B2BRestaurantApp().run()

