import flet as ft

def main(page: ft.page):
    page.window_width = 500
    page.window_height = 850
    page.bgcolor = 'white'
    #Current Week
    CurrentWeekdaySale = ft.TextField(label = " Current weekend day wise sale")
    CurrentNumberOfPple = ft.TextField(label = "Number of people received this weekend")
    #Last Week
    LastWeekdaySale = ft.TextField(label = "Last weekend day wise sale")
    LastNumberPeople = ft.TextField(label = "Number of people who visited last week")

    def Last(e):
        TotalLastWeekdaySale = int(LastWeekdaySale.value)
        TotalLastNumberPeople = int(LastNumberPeople.value)

        LastAverageSale = (TotalLastWeekdaySale) / (TotalLastNumberPeople)

        page.add(ft.Text(f"The Last Weekend's per person average sale is: {LastAverageSale}"))


    def Current(d):
        TotalCurrentWeekdaySale = int(CurrentWeekdaySale.value)
        TotalCurrentNumberOfPple = int(CurrentNumberOfPple.value)

        CurrentAverageSale = (TotalCurrentWeekdaySale) / (TotalCurrentNumberOfPple)
    
        page.add(ft.Text(f"The Current Weekend's per person average sale is: {CurrentAverageSale}"))

    submit_button = ft.ElevatedButton(text = 'CurrentAverageSale')
    submit_button2 = ft.ElevatedButton(text = 'LastAverageSaleAverageSale')

    submit_button.on_click = Current
    submit_button2.on_click = Last

    page.add(CurrentWeekdaySale)
    page.add(CurrentNumberOfPple)
    page.add(LastWeekdaySale)
    page.add(LastNumberPeople)
    page.add(submit_button)
    page.add(submit_button2)
ft.app(target = main)