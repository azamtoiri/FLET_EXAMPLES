import flet as ft


def main(page: ft.Page):
    lbl_show = ft.Text("nothing")

    page_2 = ft.Row(
        controls=[
            ft.Text(lbl_show.value),
            ft.ElevatedButton(
                'Go home',
                on_click=lambda e: page.go('/'),

            )
        ],
    )

    def submit(e):
        lbl_show.value = f'You writed... {input_.controls[0].value}'

    input_ = ft.Row(
        controls=[
            ft.TextField(
                # height=50, width=200,
                label='Write something'
            ),
            ft.ElevatedButton(
                text='Submit!',
                on_click=lambda e: page.go('/submit_page'),
            ),
        ]
    )

    pages = {
        "/": ft.View(
            "/",
            [input_]
        ),
        "/submit_page": ft.View(
            "/submit_page",
            [page_2],
        )
    }

    def route_change(route):
        page.views.clear()
        print(page.route)
        page.views.append(
            pages[page.route]
        )

    page.on_route_change = route_change
    page.go(page.route)


if __name__ == '__main__':
    ft.app(main)
