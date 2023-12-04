import flet as ft

from utils.customs import CustomInputField


class SignUp(ft.Container):
    def __init__(self,page: ft.Page):
        super().__init__()
        self.page = page
        self.expand = True
        self.page.title = "Регистрация"

        self.surname = CustomInputField(False, "Фамилия")
        self.name = CustomInputField(False, "Имя")
        self.second_name = CustomInputField(False, "Отчество")
        self.group = CustomInputField(False, "Группа")
        self.age = CustomInputField(False, "Возраст")
        self.email = CustomInputField(False, "Email")
        self.password = CustomInputField(True, "Пароль")
        self.password2 = CustomInputField(True, "Пароль")

        self.logo = ft.Image(
            src='../assets/Fox_Hub_logo.png',
            width=50,
            height=50,
        )
        self.submit_button = ft.ElevatedButton(
            width=400,
            height=45,
            text="Создать аккаунт",
            # on_click=lambda e: asyncio.run(self.validate_entries(e))
        )

        self.hav_account = ft.Text(
            value="У вас уже есть аккаунт?",
            size=15,
            color=ft.colors.with_opacity(0.50, "black")
        )

        self.login_button = ft.Container(
            alignment=ft.alignment.center,
            content=ft.Text(
                "Войти",
                color=ft.colors.with_opacity(0.50, ft.colors.BLUE)
            ),
            width=150,
            height=45,
            on_click=lambda _: page.go('/login'),
        )
        self.content = ft.Container(
            width=884, height=810,
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
                        "Регистрация",
                        size=35,
                        weight=ft.FontWeight.W_500,
                        color=ft.colors.with_opacity(0.85, "Black")

                    ),
                    ft.Row(
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        # wrap=False,
                        # scroll=ft.ScrollMode.AUTO,
                        controls=[
                            ft.Column(
                                height=400,
                                width=250,
                                controls=[
                                    self.surname,
                                    self.name,
                                    self.second_name,
                                    self.group,
                                ]
                            ),
                            ft.Column(
                                height=400,
                                width=250,
                                controls=[
                                    self.age,
                                    self.email,
                                    self.password,
                                    self.password2,
                                ]
                            ),
                        ]
                    ),
                    self.submit_button,
                    ft.Row(
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            self.hav_account,
                            self.login_button,
                        ]
                    )
                ],
            ),
        )
