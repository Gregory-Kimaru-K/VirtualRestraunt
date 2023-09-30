from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ChangeCalculatorApp(App):
    def build(self):
        self.title = "Change Calculator"

        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        # Title Label
        title_label = Label(
            text='Change Calculator',
            font_size='20sp',
            color=(1, 0, 0, 1)  # Red text color
        )
        layout.add_widget(title_label)

        # Input Fields
        invoice_number_label = Label(text='Invoice Number:')
        self.invoice_number_input = TextInput(hint_text='Enter invoice number', multiline=False)
        layout.add_widget(invoice_number_label)
        layout.add_widget(self.invoice_number_input)

        total_amount_label = Label(text='Total Invoice Amount (In Dollars):')
        self.total_amount_input = TextInput(hint_text='Enter amount in dollars', multiline=False, input_type='number')
        layout.add_widget(total_amount_label)
        layout.add_widget(self.total_amount_input)

        tip_label = Label(text='Amount of Tip (In Cents):')
        self.tip_input = TextInput(hint_text='Enter tip in cents', multiline=False, input_type='number')
        layout.add_widget(tip_label)
        layout.add_widget(self.tip_input)

        card_payment_label = Label(text='Total Payment Received by Card (In Dollars):')
        self.card_payment_input = TextInput(hint_text='Enter amount in dollars', multiline=False, input_type='number')
        layout.add_widget(card_payment_label)
        layout.add_widget(self.card_payment_input)

        service_charge_label = Label(text='Service Charge on Payment Made by Card (%):')
        self.service_charge_input = TextInput(hint_text='Enter percentage', multiline=False, input_type='number')
        layout.add_widget(service_charge_label)
        layout.add_widget(self.service_charge_input)

        cash_payment_label = Label(text='Total Payment Received in Cash (In Dollars):')
        self.cash_payment_input = TextInput(hint_text='Enter amount in dollars', multiline=False, input_type='number')
        layout.add_widget(cash_payment_label)
        layout.add_widget(self.cash_payment_input)

        # Calculate Button
        calculate_button = Button(text='Calculate Change', on_press=self.calculate_change)
        layout.add_widget(calculate_button)

        # Result Label
        self.result_label = Label(text='', font_size='18sp')
        layout.add_widget(self.result_label)

        return layout

    def calculate_change(self, instance):
        try:
            total_amount_dollars = float(self.total_amount_input.text)
            tip_cents = int(self.tip_input.text)
            card_payment_dollars = float(self.card_payment_input.text)
            service_charge_percentage = float(self.service_charge_input.text)
            cash_payment_dollars = float(self.cash_payment_input.text)

            # Calculate Total Payment
            total_payment_dollars = (card_payment_dollars * (1 + service_charge_percentage / 100)) + cash_payment_dollars

            # Calculate Change
            change_dollars = total_payment_dollars - (total_amount_dollars + tip_cents / 100)

            if change_dollars >= 0:
                self.result_label.text = f"Change to be returned (In Dollars): ${change_dollars:.2f}"
            else:
                self.result_label.text = "Outstanding amount."
        except ValueError:
            self.result_label.text = "Invalid input. Please enter valid numbers."

if __name__ == '__main__':
    ChangeCalculatorApp().run()

