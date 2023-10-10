import flet as ft

def main(page: ft.page):
    page.window_width = 500
    page.window_height = 850
    page.bgcolor = "white"

    
    order_base_cost = ft.TextField(label = "Insert your order base cost")
    order_type_select = ft.TextField(label = "Order Type (1: dine in, 2: pick up, 3: delivery)")

    def calculate_total_charges(p):

        try:
            base_cost = float(order_base_cost.value)
            order_type = int(order_type_select.value)

            if order_type == 1:
                total_charges = base_cost * 1.08

            elif order_type == 3:
                total_charges = base_cost * 1.10

            else:
                total_charges = base_cost

            page.add(ft.Text(value = f"Total charges are: {total_charges: .2f} AUD"))
        
        except ValueError:
            page.add(ft.Text(value = "Please enter a numeric value"))

    calculate_button = ft.ElevatedButton(text = "Total charge")

    calculate_button.on_click = calculate_total_charges

    page.add(order_base_cost)
    page.add(order_type_select)
    page.add(calculate_button)

ft.app(target = main)