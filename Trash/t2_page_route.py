import flet as ft


# TODO: Сделать несколько страниц по которым можно перемещаться и возвращаться обратно
def main(page: ft.Page):
    page.title = "Page routing"
    page.add(ft.Text(f"First page: {page.route}"))

    login_form = ft.Row(controls=[
        ft.AppBar(title=ft.Text("Route testing"), bgcolor=ft.colors.SURFACE_VARIANT),
        ft.Text("Login Page"),
        ft.ElevatedButton('Go to register', on_click=lambda e: page.go('/register'))
    ])

    register_form = ft.Row(controls=[
        ft.AppBar(title=ft.Text("Route testing"), bgcolor=ft.colors.SURFACE_VARIANT),
        ft.Text("Register Page"),
        ft.ElevatedButton('Go to login', on_click=lambda e: page.go('/login'))
    ])

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        page.views.append(
            ft.View(
                '/',
                [
                    ft.AppBar(title=ft.Text("Route testing"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.Column(
                        controls=[
                            ft.Text('Main page'),
                            ft.ElevatedButton('Login', on_click=lambda e: page.go('/login')),
                            ft.ElevatedButton('Register', on_click=lambda e: page.go('/register'))
                        ]
                    )
                ]
            )
        )

        if page.route == '/login':
            page.views.append(
                login_form
            )
        elif page.route == '/register':
            page.views.append(
                register_form
            )
        print(page.route)
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER)
