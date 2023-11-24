from flet import *

from custom_checkbox import CustomCheckBox

BG = "#041955"
FWG = '#94b4ff'
FG = "#3450a1"
PINK = "#eb06ff"


def main(page: Page):
    page.window_width = 450
    page.window_height = 910
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    circle = Stack(
        controls=[
            Container(
                width=100,
                height=100,
                border_radius=50,
                bgcolor=colors.WHITE12
            ),
            Container(
                gradient=SweepGradient(
                    center=alignment.center,
                    start_angle=0.0,
                    end_angle=3,
                    stops=[0.5, 0.5],
                    colors=['#0000000000', PINK]
                ),
                width=100,
                height=100,
                border_radius=50,
                content=Row(
                    alignment=alignment.center,
                    controls=[
                        Container(
                            padding=padding.all(5),
                            bgcolor=BG,
                            width=90, height=90,
                            border_radius=50,
                            content=Container(
                                bgcolor=FG,
                                height=80, width=80,
                                border_radius=40,
                                content=CircleAvatar(
                                    opacity=0.8,
                                    foreground_image_url="https://images.unsplash.com/photo-1545912452-8aea7e25a3d3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
                                )
                            )
                        )
                    ]
                )
            )
        ]
    )

    def shrink(e):
        page_2.controls[0].width = 120
        page_2.controls[0].scale = transform.Scale(
            0.8, alignment=alignment.center_right
        )
        page_2.controls[0].border_radius = border_radius.only(
            top_left=35,
            top_right=0,
            bottom_left=35,
            bottom_right=0
        )
        page_2.update()

    def restore(e):
        page_2.controls[0].width = 400
        page_2.controls[0].border_radius = 35
        page_2.controls[0].scale = transform.Scale(
            1, alignment=alignment.center_right
        )
        page_2.update()

    create_task_view = Container(
        content=Container(
            height=40, width=40,
            content=Text('X', width=50, height=50),
            on_click=lambda _: page.go('/'),
        )
    )

    tasks = Column(
        height=400,
        scroll=ScrollMode.AUTO,
    )

    for i in range(10):
        tasks.controls.append(
            Container(
                height=70,
                width=400,
                bgcolor=BG,
                padding=padding.only(top=25, left=20),
                border_radius=25,
                content=CustomCheckBox(
                    PINK,
                    label='Add somthing interesting',
                    size=30,
                ),
            ),
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
                        Container(content=Icon(icons.MENU), on_click=lambda e: shrink(e)),
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

    page_1 = Container(
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=35,
        padding=padding.only(left=50, top=60, right=200),

        content=Column(
            controls=[
                Row(
                    alignment='end',
                    controls=[
                        Container(
                            border_radius=25,
                            padding=padding.only(
                                top=13, left=13,
                            ),
                            height=50,
                            width=50,
                            border=border.all(color='white', width=2),
                            on_click=lambda e: restore(e),
                            content=Text('<'),
                        )
                    ]
                ),
                Container(height=20),
                Text('Olivia\nMitchel', size=32, weight='bold'),
                circle,
            ]
        )
    )
    page_2 = Row(alignment='end',
                 controls=[
                     Container(
                         width=400,
                         height=850,
                         bgcolor=FG,
                         border_radius=35,
                         animate=animation.Animation(600, AnimationCurve.DECELERATE),
                         animate_scale=animation.Animation(400, curve='decelerate'),
                         padding=padding.only(
                             top=50, left=20,
                             right=20, bottom=5
                         ),
                         content=Column(
                             controls=[
                                 first_page_contents
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
        page.views.clear()
        page.views.append(
            pages[page.route]
        )

    page.on_route_change = route_change
    page.go(page.route)


if __name__ == '__main__':
    app(target=main)
