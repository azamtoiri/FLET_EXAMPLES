import flet as ft

from master_project.utils.Customs import CustomInputField


class SignInForm(ft.UserControl):
    def __init__(self, logo_path: str):
        super().__init__()

        self.email = CustomInputField(False, "Email")
        self.password = CustomInputField(True, "Password")

        self.logo = ft.Image(
            src=logo_path,
            width=50,
            height=50,
        )
        self.submit_button = ft.ElevatedButton(
            width=400,
            height=45,
            text="Войти",
            # on_click=lambda e: asyncio.run(self.validate_entries(e))
        )

        self.no_account = ft.Text(
            "Еще нет аккаунта?",
            size=15,
            color=ft.colors.with_opacity(0.50, "black")
        )

        self.create_account_button = ft.Container(
            alignment=ft.alignment.center,
            content=ft.Text(
                "Регистрация",
                color=ft.colors.with_opacity(0.50, ft.colors.BLUE)
            ),
            width=150,
            height=45,
            on_click=lambda e: print(e),
        )

    def build(self):
        return ft.Container(
            width=450, height=650,
            bgcolor=ft.colors.with_opacity(1, "white"),
            border_radius=10,
            padding=40,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    self.logo,
                    ft.Text(
                        "FoxHub",
                        size=21,
                        weight=ft.FontWeight.W_800,
                        color=ft.colors.with_opacity(1, "Black")
                    ),
                    ft.Text(
                        "Вход",
                        size=35,
                        weight=ft.FontWeight.W_800,
                        color=ft.colors.with_opacity(0.85, "Black")

                    ),
                    ft.Divider(height=15, color=ft.colors.TRANSPARENT),
                    ft.Text(
                        "Введите ваш email и пароль",
                        color=ft.colors.with_opacity(1, "Black")
                    ),
                    self.email,
                    ft.Divider(height=5, color=ft.colors.TRANSPARENT),
                    self.password,
                    ft.Divider(height=25, color=ft.colors.TRANSPARENT),
                    self.submit_button,
                    ft.Row(
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            self.no_account, self.create_account_button,
                        ]
                    )
                ],
            ),
        )
