import flet as ft
import math

def main(page: ft.page):
    page.window_width = 500
    page.window_height = 850
    page.bgcolor = "White"
    
    EmployeePosition = ft.TextField(label = "EmployeePosition")
    NumberofHours = ft.TextField(label = "Number of employee Month Hours")

    def Calculate_income(d):
        Employee = ((EmployeePosition.value).lower())
        MonthlyHours = math.ceil(float(NumberofHours.value))

        if Employee == "chef":
            MonthIncome = ((30 * MonthlyHours) * 0.82)
            page.add(ft.Text(value = f"Income of Chef is: ${MonthIncome: .2f}"))

        elif Employee == "waiter":
            MonthIncome = ((28 * MonthlyHours) * 0.82)
            page.add(ft.Text(value = f"Income of Waiter is: ${MonthIncome: .2f}"))

        elif Employee == "delivery":
            MonthIncome = ((25 * MonthlyHours) * 0.82)
            page.add(ft.Text(value = f"Income of Delivery is: ${MonthIncome: .2f}"))

        elif Employee == "cleaner":
            MonthIncome = ((24 * MonthlyHours) * 0.82)
            page.add(ft.Text(value = f"Income of Chef is: ${MonthIncome: .2f}"))

    income_button = ft.ElevatedButton(text = "Calculate Income")

    income_button.on_click = Calculate_income
    
    page.add(EmployeePosition)
    page.add(NumberofHours)
    page.add(income_button)

ft.app(target = main)