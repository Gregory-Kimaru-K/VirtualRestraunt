import flet as ft
import re

def main(page: ft.page):
    page.window_width = 500
    page.window_height = 850
    page.bgcolor = "White"
    
    Mobile_Number = ft.TextField(label = "Enter Your Mobile Number: ")
    password = ft.TextField(label = "Enter password: ")

    def auth(p):
        try:
            MobileNum = Mobile_Number.value
            pwd = password.value

            if not (len(MobileNum) == 10 and (MobileNum).isdigit()):
                page.add(ft.Text(value = "Invalid Credentials1"))
                return
            
            if not (7 <= len(pwd) <= 11 and re.search(r'[@$]', pwd) and pwd[-1].isdigit()):
                page.add(ft.Text(value = "Invalid Credentials2"))
                return
            
            page.add(ft.Text(value = "Valid Credentials"))
            

        except ValueError:
            page.add(ft.Text(value = "Invalid credentials4"))

    auth_button = ft.ElevatedButton(text = "Authenticate")
    auth_button.on_click = auth

    page.add(Mobile_Number)
    page.add(password)
    page.add(auth_button)

ft.app(target = main)