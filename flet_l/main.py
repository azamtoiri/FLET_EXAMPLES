import flet as ft


def box_style(theme: ft.Page.theme_mode) -> dict:
    return {
        "width": 100,
        "height": 100,
        "bgcolor": "teal" if theme == "dark" else "pink",
        "border_radius": 10,
    }


def main(page: ft.Page):
    page.title = "Containers with background color"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.theme_mode = ft.ThemeMode.DARK

    c1 = ft.Container(
        content=ft.ElevatedButton("Elevated button in cont"),
        bgcolor=ft.colors.YELLOW,
        padding=5,
    )

    c2 = ft.Container(
        content=ft.ElevatedButton("Elevated button in cont, opacity 0.5"),
        bgcolor=ft.colors.BLUE,
        padding=5,
        opacity=0.5,
    )

    c3 = ft.Container(
        content=ft.OutlinedButton("Outlined button in container"),
        bgcolor=ft.colors.TEAL,
        padding=5,
    )

    page.add(
        c1, c2, c3,
        ft.Container(
            width=100,
            height=100,
            bgcolor="teal",
            border_radius=6
        ),
        ft.Container(**box_style(page.theme_mode))
    )
    page.update()


if __name__ == '__main__':
    ft.app(target=main)
