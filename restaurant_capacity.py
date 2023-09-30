from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class RestaurantCapacityApp(App):
    def build(self):
        self.title = 'Restaurant Capacity Calculator'

        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Title Label
        title_label = Label(
            text='B2B Restaurant Capacity Calculator',
            font_size='20sp',
            color=(1, 0, 0, 1)  # Red text color
        )
        layout.add_widget(title_label)

        # Width Input
        width_label = Label(text='Enter Restaurant Width (cm):')
        self.width_input = TextInput(hint_text='Enter width', input_type='number', multiline=False)
        layout.add_widget(width_label)
        layout.add_widget(self.width_input)

        # Length Input
        length_label = Label(text='Enter Restaurant Length (cm):')
        self.length_input = TextInput(hint_text='Enter length', input_type='number', multiline=False)
        layout.add_widget(length_label)
        layout.add_widget(self.length_input)

        # Calculate Button
        calculate_button = Button(text='Calculate Capacity', on_press=self.calculate_capacity)
        layout.add_widget(calculate_button)

        # Capacity Label
        self.capacity_label = Label(text='', font_size='18sp')
        layout.add_widget(self.capacity_label)

        return layout

    def calculate_capacity(self, instance):
        try:
            width_cm = float(self.width_input.text)
            length_cm = float(self.length_input.text)

            # Calculate capacity in square meters
            square_meters = (width_cm * length_cm) / 10000  # Convert cm² to m²

            # Calculate the maximum number of customers (1.3 square meters per customer)
            max_customers = int(square_meters / 1.3)

            self.capacity_label.text = f'Maximum Capacity: {max_customers} customers'
        except ValueError:
            self.capacity_label.text = 'Invalid input. Please enter valid numbers.'

if __name__ == '__main__':
    RestaurantCapacityApp().run()

