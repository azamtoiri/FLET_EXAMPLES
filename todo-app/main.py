from flet import *

BG = "#041955"
FWG = '#94b4ff'
FG = "#3450a1"
PINK = "#eb06ff"


def main(page: Page):
    page.window_width = 450
    page.window_height = 910
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    create_task_view = Container(
        content=Container(
            height=40, width=40,
            content=Text('x'),
            on_click=lambda _: page.go('/'),
            # bgcolor=FG,
        )
    )

    tasks = Column(
        height=400,
        scroll=ScrollMode.AUTO,
    )

    for i in range(10):
        tasks.controls.append(
            Container(height=70, width=400, bgcolor=BG, border_radius=25),
        )

    # card categories which we see
    categories_card = Row(
        scroll=ScrollMode.AUTO,
    )

    # the categories that he add to cat_card
    categories = ['Business', 'Family', 'Friend']
    for i, category in enumerate(categories):
        categories_card.controls.append(
            Container(
                width=170,
                height=110,
                bgcolor=BG,
                border_radius=20,
                padding=15,
                content=Column(
                    controls=[
                        Text('40 Task'),
                        Text(category),
                        Container(
                            width=160,
                            height=5,
                            bgcolor='white12',
                            border_radius=20,
                            padding=padding.only(right=i * 30),
                            content=Container(
                                bgcolor=PINK,
                            ),
                        )
                    ]
                )
            )
        )

    first_page_contents = Container(
        content=Column(
            controls=[
                Row(
                    alignment='spaceBetween',
                    controls=[
                        Container(content=Icon(icons.MENU)),
                        Row(controls=[
                            Icon(icons.SEARCH),
                            Icon(icons.NOTIFICATIONS_OUTLINED)
                        ])
                    ]
                ),
                Container(height=25),
                Text(value='Hello, Azam'),
                Text(value='CATEGORIES'),
                Container(
                    padding=padding.only(top=10, bottom=20, ),
                    content=categories_card,
                ),
                Container(height=20),
                Text("TODAY'S TASKS"),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton(
                            bottom=2, right=20,
                            icon=icons.ADD,
                            on_click=lambda _: page.go('/create_task')
                        )
                    ]
                )
            ]
        )
    )

    page_1 = Container()
    page_2 = Row(
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor=FG,
                border_radius=35,
                padding=padding.only(
                    top=50, left=20,
                    right=20, bottom=5,
                ),
                content=Column(
                    controls=[
                        first_page_contents,
                    ]
                )
            )
        ]
    )

    container_ = Container(
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=35,
        content=Stack(
            controls=[
                page_1,
                page_2,
            ]
        )
    )

    pages = {
        "/": View(
            "/",
            [
                container_
            ],
        ),
        "/create_task": View(
            "/create_task",
            [
                create_task_view
            ]
        )
    }

    def route_change(route):
        # pass
        page.views.clear()
        page.views.append(
            pages[page.route]
        )

    page.add(container_)

    page.on_route_change = route_change
    page.go(page.route)


if __name__ == '__main__':
    app(target=main)
