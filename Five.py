import flet as ft

def main(page: ft.page):
    page.window_width = 500
    page.window_height = 850
    page.bgcolor = 'white'

    FullAddress = ft.TextField(label = "Address")
    OrderAmount = ft.TextField(label = "Amount of order placed")
    Distance  = ft.TextField(label = "Distance Between the address and Resturaunt")

    def total_charges(d):
        Address = FullAddress.value
        Amount = int(OrderAmount.value) if OrderAmount.value else 0
        TotalDistance = int(Distance.value)

        pack = 0
        delv = 0

        #Packaging charges
        if Amount >20 and Amount >= 35:
            pack = Amount * 0.1
        
        elif Amount > 35 and Amount >= 50:
            pack = Amount * 0.08

        elif Amount > 50:
            pack = Amount * 0.06

        #Delivery charges
        if TotalDistance > 0 and TotalDistance <= 4:
            delv = 3

        if TotalDistance > 4 and TotalDistance <= 8:
            delv = 6

        if TotalDistance > 8 and TotalDistance <= 12:
            delv = 8

        if TotalDistance > 12:
            page.add(ft.Text("No Delivery can be done"))

        page.add(ft.Text(f"Packaging charge is: {pack}"))
        page.add(ft.Text(f"Delivery charge is: {delv}"))
        page.add(ft.Text(f"Total charge is: {pack + delv}"))

    submit_button = ft.ElevatedButton(text = "Calculate charges")
    submit_button.on_click = total_charges

    page.add(FullAddress)
    page.add(OrderAmount)
    page.add(Distance)
    page.add(submit_button)
ft.app(target = main)