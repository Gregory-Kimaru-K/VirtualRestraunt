import flet as ft 

def main(page: ft.page):
    page.window_width = 500
    page.widow_height = 850
    page.bgcolor = "white"

    
ft.app(target = main)