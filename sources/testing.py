import flet
import flet as ft


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    print("initial route: ", page.route)

    def open_settings(e):
        page.go("/settings")

    def open_main_settings(e):
        page.go("/settings/mail")

    def route_change(e):
        print("Route change: ", e.route)
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                controls=[
                    ft.AppBar(title=ft.Text("Flet App")),
                    ft.ElevatedButton("Got to settings", on_click=open_settings),
                    ft.ElevatedButton("Go to mail settings", on_click=open_main_settings),
                ]
            )
        )
        if page.route == "/settings" or page.route == "settings/mail":
            page.views.append(
                ft.View(
                    "/settings",
                    controls=[
                        ft.AppBar(title=ft.Text("Settings"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.Text("Settings!", style="bodyMedium"),
                        ft.ElevatedButton("Go to mail settings", on_click=open_main_settings)
                    ]
                )
            )
        if page.route == "/settings/mail":
            page.views.append(
                ft.View(
                    "/settings/mail",
                    controls=[
                        ft.AppBar(
                            title=ft.Text("Mail settings"), bgcolor=ft.colors.SURFACE_VARIANT,
                        ),
                        ft.Text("Mail settings!"),
                        ft.ElevatedButton("Go to settings", on_click=open_settings),
                    ],
                )
            )
        page.update()

    def view_pop(e):
        print("View pop:", e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop


    side_bar = ft.Row(
        controls=[
            ft.Column(
                controls=[
                    ft.ElevatedButton("1-st page"),
                    ft.ElevatedButton("2-nd page"),
                    ft.ElevatedButton("3-nd page"),
                    ft.ElevatedButton("4-nd page"),
                ],
            )
        ],
    )

    # page.add(side_bar)
    # page.update()
    page.go(page.route)


if __name__ == '__main__':
    ft.app(main)
