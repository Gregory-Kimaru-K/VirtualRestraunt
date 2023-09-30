import flet as ft

def main(page: ft.page):
    page.window_width = 500
    page.window_height = 850
    page.bgcolor = 'white'

    Name = ft.TextField(label="Name")
    MobileNumber = ft.TextField(label="Mobile Number")
    Birth = ft.TextField(label="Date of Birth")
    City = ft.TextField(label="City")
    Email = ft.TextField(label="Enter your email")

    submit_button = ft.ElevatedButton(text="Submit", color="blue")

    def submit_form(d):
        userName = Name.value
        UserMobileNumber = MobileNumber.value
        BirthYr = Birth.value
        City_liv = City.value
        UserEmail = Email.value

        if userName and UserMobileNumber and BirthYr and City_liv and UserEmail:
            if (2023 - int(BirthYr)) >= 21:
                page.add(ft.Text(value=f"Hello {userName}"))
                page.add(ft.Text(value=f"These are the details you provided:"))
                page.add(ft.Text(value=f"Name: {userName}"))
                page.add(ft.Text(value=f"Mobile Number: {UserMobileNumber}"))
                page.add(ft.Text(value=f"Year of birth: {BirthYr}"))
                page.add(ft.Text(value=f"City: {City_liv}"))
                page.add(ft.Text(value=f"Email: {UserEmail}"))
            else:
                page.add(ft.Text(value="Some details are missing, please enter them"))
        else:
            page.add(ft.Text(value="Please enter all the details."))

    submit_button.on_click = submit_form

    page.add(Name)
    page.add(MobileNumber)
    page.add(Birth)
    page.add(City)
    page.add(Email)
    page.add(submit_button)

ft.app(target=main)
