from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import datetime  # Import the datetime module
from kivy.lang import Builder

# Use a KV language file for improved organization (stylish.kv)
kv = """
BoxLayout:
    orientation: 'vertical'
    spacing: '10dp'
    padding: '20dp'
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1  # White background color
        Rectangle:
            pos: self.pos
            size: self.size
    Label:
        text: 'Customer Name:'
        size_hint: None, None
        height: '30dp'
        color: 1, 0, 0, 1  # Red text color
    TextInput:
        hint_text: 'Enter your name'
        multiline: False
        background_color: 1, 1, 1, 0.8  # White input field with slight transparency
    Label:
        text: 'Mobile Number:'
        size_hint: None, None
        height: '30dp'
        color: 1, 0, 0, 1  # Red text color
    TextInput:
        hint_text: 'Enter your mobile number'
        multiline: False
        background_color: 1, 1, 1, 0.8  # White input field with slight transparency
    # Add styling for other input fields, buttons, and labels as needed
    Label:
        id: greeting_label
        text: ''
        size_hint: None, None
        height: '30dp'
        color: 1, 0, 0, 1  # Red text color
    Button:
        text: 'Submit'
        on_press: app.calculate_age_and_greet()
        background_color: 1, 0, 0, 1  # Red button color
"""

class StylishCustomerDetailsApp(App):
    def build(self):
        return Builder.load_string(kv)

class CustomerDetailsApp(App):
    def build(self):
        self.title = 'Customer Details'
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Customer Name Input
        name_label = Label(text='Customer Name:')
        self.name_input = TextInput(hint_text='Enter your name', multiline=False)
        layout.add_widget(name_label)
        layout.add_widget(self.name_input)

        # Mobile Number Input
        mobile_label = Label(text='Mobile Number:')
        self.mobile_input = TextInput(hint_text='Enter your mobile number', multiline=False)
        layout.add_widget(mobile_label)
        layout.add_widget(self.mobile_input)

        # Year of Birth Input
        birth_label = Label(text='Year of Birth:')
        self.birth_input = TextInput(hint_text='Enter your birth year', multiline=False)
        layout.add_widget(birth_label)
        layout.add_widget(self.birth_input)

        # Current City Input
        city_label = Label(text='Current City:')
        self.city_input = TextInput(hint_text='Enter your city', multiline=False)
        layout.add_widget(city_label)
        layout.add_widget(self.city_input)

        # Email Address Input
        email_label = Label(text='Email Address:')
        self.email_input = TextInput(hint_text='Enter your email address', multiline=False)
        layout.add_widget(email_label)
        layout.add_widget(self.email_input)

        # Greeting Label (To display the greeting message)
        self.greeting_label = Label(text='', size_hint=(1, None), height=30)
        layout.add_widget(self.greeting_label)

        # Create a button to trigger the greeting message
        greeting_button = Button(text='Submit', on_press=self.calculate_age_and_greet)
        layout.add_widget(greeting_button)

        return layout

    def calculate_age_and_greet(self, instance):
        name = self.name_input.text.strip()
        mobile = self.mobile_input.text.strip()
        birth_year = self.birth_input.text.strip()
        city = self.city_input.text.strip()
        email = self.email_input.text.strip()

        # Calculate age (assuming the current year is always 2023)
        if birth_year.isdigit():
            birth_year = int(birth_year)
            current_year = datetime.datetime.now().year
            age = current_year - birth_year

            if age > 21:
                greeting = f'Hello {name}!\nYou are {age} years old.'
            else:
                greeting = f'Hello {name}!\nYou must be at least 21 years old to use this service.'
        else:
            greeting = f'Hello {name}!\nInvalid birth year entered.'

        self.greeting_label.text = greeting

if __name__ == '__main__':
    CustomerDetailsApp().run()

