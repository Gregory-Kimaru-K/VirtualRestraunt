import flet as ft

def main(page: ft.page):
    page.window_width = 500
    page.window_height = 850
    page.bgcolor = 'white'

    page.add(ft.Text(value = "Please input the length of your restraunt in cm"))
    restraunt_width = ft.TextField(label = "width")

    restraunt_length = ft.TextField(label = "Length")

    def calculate_area(d):
        width = int(restraunt_width.value)
        length = int(restraunt_length.value)

        area = (width * length) / 10000

        if width and length or length == 0 or width == 0:
            if (area / 1.3) < 70:
                restrauntCapacity = int(area / 1.3)
                page.add(ft.Text(f"Resturant can accomodate: {restrauntCapacity} people"))
            
            else:
                page.add(ft.Text("Resturant can only accomodate 70 people"))

    submit_button = ft.ElevatedButton(text = "Estimate number of people restaurant can accomodate")
    submit_button.on_click = calculate_area

    page.add(restraunt_width)
    page.add(restraunt_length)
    page.add(submit_button)

ft.app(target=main)