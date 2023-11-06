import flet as ft
import flet_material as fm

PRIMARY = ft.colors.TEAL

fm.Theme.set_theme(theme=PRIMARY)

# user login and password
dummy_user_list: list = [["dummy@gmail.com"], 121212]


class CustomInputField(ft.UserControl):
    def __init__(self, password: bool, title: str):
        self.input: ft.Control = ft.TextField(
            height=50,
        )
        self.input_box: ft.Container = ft.Container(
            expand=True,
            content=self.input,
            animate=ft.Animation(300, ft.animation.AnimationCurve.EASE),
            shadow=None,
        )
        self.object = self.create_input(title)

        super().__init__()

    def create_input(self, title):
        return ft.Column(
            spacing=5,
            controls=[
                ft.Text(title, size=11, weight=ft.FontWeight.BOLD, color="#bbbbbb"),
                ft.Stack(
                    controls=[
                        self.input_box,
                        # status...
                    ],
                )
                # loader ...
            ],
        )

    def build(self):
        return self.object


# Mian form class: stores the major instances
class MainFormUI(ft.UserControl):
    def __init__(self):
        self.email = CustomInputField(False, "Email")
        self.password = CustomInputField(False, "Password")
        super().__init__()

    def build(self):
        return ft.Container(
            width=450, height=550,
            bgcolor=ft.colors.with_opacity(0.01, "white"),
            border_radius=10,
            padding=40,
            content=ft.Column(
                horizontal_alignment=ft.alignment.center,
                alignment=ft.alignment.center,
                controls=[
                    ft.Text(
                        "Validating Signin Form - Flet",
                        size=21,
                        weight=ft.FontWeight.W_800,
                        color=ft.colors.with_opacity(0.85, "white")
                    ),
                    ft.Divider(height=25, color=ft.colors.TRANSPARENT),
                    self.email,
                    self.password,
                    ft.Divider(height=25, color=ft.colors.TRANSPARENT),
                ],
            ),
        )


def main(page: ft.Page):
    page.bgcolor = fm.Theme.bgcolor

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    form = MainFormUI()
    page.add(form)
    page.update()


if __name__ == '__main__':
    ft.app(target=main)
