import flet as ft

def  Centigrade_to_Fahrenheit(Celsius):
    return ((Celsius * 1.8) + 32)

def  Fahrenheit_to_Centigrade(Fahrenheit):
    return ((Fahrenheit - 32) * 1.8)

def main(page: ft.page):
    page.window_width = 500
    page.window_height = 850
    page.bgcolor = "white"

    temp_value = ft.TextField(label = "Enter Temperature")
    Convertion_type = ft.TextField(label = "From C to F enter 1 From F to C enter 2")

    
    def convert_temp(p):
        try:
            temp = float(temp_value.value)
            option = int(Convertion_type.value)

            if option == 1:
                convert_temp = Centigrade_to_Fahrenheit(temp)
                page.add(ft.Text(value = f"Converted temperature: {convert_temp: .2f}"))

            elif option == 2:
                convert_temp = Fahrenheit_to_Centigrade(temp)
                page.add(ft.Text(value = f"Converted temperature: {convert_temp: .2f}"))

            else:
                page.add(ft.Text(value = "Invalid choice. Please choose a valid temp conversion (1 or 2): "))

        except:
            page.add(ft.Text(value = "Invalid temp. Please choose a temperature value"))

    convert_button = ft.ElevatedButton(text = "Convert")

    convert_button.on_click = convert_temp

    page.add(temp_value)
    page.add(Convertion_type)
    page.add(convert_button)


ft.app(target = main)