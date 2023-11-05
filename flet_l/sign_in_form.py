import flet as ft
import flet_material as fm

PRIMARY = ft.colors.TEAL

fm.Theme.set_theme(theme=PRIMARY)

# user login and password
dummy_user_list: list = [["dummy@gmail.com"], 121212]


def main(page: ft.Page):
    page.bgcolor = fm.Theme.bgcolor

    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER

    page.update()


if __name__ == '__main__':
    ft.app(target=main)
