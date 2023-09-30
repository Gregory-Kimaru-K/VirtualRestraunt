from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class WeekendSalesApp(App):
    def build(self):
        self.title = "Weekend Sales Assessment"

        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Title Label
        title_label = Label(
            text='B2B Weekend Sales Assessment',
            font_size='20sp',
            color=(1, 0, 0, 1)  # Red text color
        )
        layout.add_widget(title_label)

        # Input Fields for Current Weekend
        current_weekend_label = Label(
            text='Enter Current Weekend Sales (comma-separated) and Visitors:'
        )
        self.current_weekend_input = TextInput(hint_text='Sales, Visitors', multiline=False)
        layout.add_widget(current_weekend_label)
        layout.add_widget(self.current_weekend_input)

        # Input Fields for Last Weekend
        last_weekend_label = Label(
            text='Enter Last Weekend Sales (comma-separated) and Visitors:'
        )
        self.last_weekend_input = TextInput(hint_text='Sales, Visitors', multiline=False)
        layout.add_widget(last_weekend_label)
        layout.add_widget(self.last_weekend_input)

        # Calculate Button
        calculate_button = Button(text='Calculate Averages', on_press=self.calculate_averages)
        layout.add_widget(calculate_button)

        # Result Labels
        self.current_average_label = Label(text='', font_size='18sp')
        layout.add_widget(self.current_average_label)

        self.last_average_label = Label(text='', font_size='18sp')
        layout.add_widget(self.last_average_label)

        return layout

    def calculate_averages(self, instance):
        current_weekend_data = self.current_weekend_input.text.strip().split(',')
        last_weekend_data = self.last_weekend_input.text.strip().split(',')

        if len(current_weekend_data) != 2 or len(last_weekend_data) != 2:
            self.current_average_label.text = 'Invalid input format.'
            self.last_average_label.text = ''
            return

        try:
            current_sales, current_visitors = map(float, current_weekend_data)
            last_sales, last_visitors = map(float, last_weekend_data)

            current_average = current_sales / current_visitors
            last_average = last_sales / last_visitors

            self.current_average_label.text = f'Current Weekend Average: ${current_average:.2f} per person'
            self.last_average_label.text = f'Last Weekend Average: ${last_average:.2f} per person'
        except ValueError:
            self.current_average_label.text = 'Invalid input. Please enter valid numbers.'
            self.last_average_label.text = ''

if __name__ == '__main__':
    WeekendSalesApp().run()

