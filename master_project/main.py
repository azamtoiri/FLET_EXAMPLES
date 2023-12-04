import flet as ft
from flet import Page, View

from pages import Login, SignUp, Welcome

LOGO_PATH = '../assets/Fox_Hub_logo.png'


class Main(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page
        self.init_helper()

    def init_helper(self):
        self.page.on_route_change = self.on_route_change
        self.page.go('/')

    def on_route_change(self, route):
        new_page = {
            "/": Welcome,
            "/login": Login,
            "/signup": SignUp,
            # "/me": Dashboard,
            # "/forgotpassword": ForgotPassword,
        }[self.page.route](self.page)
        # print(new_page.page)

        self.page.views.clear()
        self.page.views.append(
            View(
                route,
                [new_page]
            )
        )


def main(page: Page):
    page.visible = True
    page.title = "Главная страница"
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "Open Sans": "/fonts/OpenSans-Regular.ttf"
    }
    page.window_width = 1000
    page.window_height = 1000

    # region: Main page

    main_page = ft.Container(
        width=600,
        height=505,
        bgcolor=ft.colors.with_opacity(1, "white"),
        border_radius=10,
        padding=40,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            # alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Image(
                    width=100,
                    height=100,
                    src='../assets/Fox_Hub_logo.png'
                ),
                ft.Text(
                    "FoxHub",
                    size=21,
                    weight=ft.FontWeight.W_800,
                    color=ft.colors.with_opacity(1, "Black")
                ),
                ft.Text(
                    value="Добро пожаловать!",
                    size=35,
                    weight=ft.FontWeight.W_500,
                    color=ft.colors.with_opacity(0.85, "Black"),
                    text_align=ft.alignment.center,
                ),
                ft.Row(
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.ElevatedButton(
                            text='Войти',
                            on_click=lambda _: page.go('/login'),
                        ),
                        ft.ElevatedButton(
                            text='Регистрация',
                            on_click=lambda _: page.go('/register')
                        ),
                    ]
                )
            ],
        ),
    )
    # endregion

    app_bar: ft.AppBar = ft.AppBar(bgcolor=ft.colors.SURFACE_VARIANT, )

    sign_in_form = Login(
        logo_path=LOGO_PATH,
        page=page,
    )

    register_form = SignUp(
        logo_path=LOGO_PATH,
        page=page,
    )

    sign_in_form.page.title = "Вход"
    register_form.page.title = "Регистрация"

    # region: other navigation
    pages = {
        '/': View(
            "/",
            [
                app_bar,
                main_page
            ],
        ),
        '/login': View(
            '/login',
            [
                app_bar,
                sign_in_form,
            ]
        ),
        '/register': View(
            'register',
            [
                app_bar,
                register_form
            ]
        )
    }

    # endregion

    def route_change(route):
        page.views.clear()
        # print(page.route)
        page.views.append(
            View(
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                route="/",
                controls=[
                    ft.AppBar(bgcolor=ft.colors.SURFACE_VARIANT, ),
                    main_page
                ],
            )
        )
        if page.route == '/login':
            page.views.append(
                View(
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    route='/login',
                    controls=[
                        ft.AppBar(bgcolor=ft.colors.SURFACE_VARIANT, ),
                        sign_in_form,
                    ]
                )
            )
        if page.route == '/register':
            page.views.append(
                View(
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    route='/register',
                    controls=[
                        ft.AppBar(bgcolor=ft.colors.SURFACE_VARIANT, ),
                        register_form
                    ]
                )
            )

    def view_pop(e):
        print("View pop:", e.view)
        page.views.pop()
        top_view = page.views[0]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == '__main__':
    ft.app(target=Main, host="192.168.0.112", port=58735)

# TODO:
#  Fix page navigation
