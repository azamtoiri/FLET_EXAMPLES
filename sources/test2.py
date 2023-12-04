import flet as ft


def main(page: ft.Page):
    page.title = "Headspace clone"

    def change_content(e):
        page.controls.clear()
        nav_dest = e.control.selected_index

        if nav_dest == 0:
            nav_content = ft.Container(
                content=ft.Text(value="Today")
            )
            page.add(nav_content)

        if nav_dest == 1:
            nav_content = ft.Container(
                content=ft.Text(value="Explore")
            )
            page.add(nav_content)

        if nav_dest == 2:
            nav_content = ft.Container(
                content=ft.Text(value="You")
            )
            page.add(nav_content)

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.LANDSCAPE_OUTLINED,
                selected_icon=ft.icons.LANDSCAPE,
                label="Today"
            ),
            ft.NavigationDestination(
                icon=ft.icons.SEARCH,
                label="Explore"
            ),
            ft.NavigationDestination(
                icon=ft.icons.PERSON_OUTLINED,
                selected_icon=ft.icons.PERSON,
                label="You"
            )
        ],
        on_change=change_content,
        selected_index=0
    )

    # a control's did_mount() is invoked right after it has been mounted
    page.navigation_bar.did_mount = lambda: synthetic_event(
        page=page, control=page.navigation_bar
    )

    # call the did_mount() once manually if you mess up the order of page.update()
    # page.navigation_bar.did_mount()
    page.update()


def synthetic_event(page: ft.Page, control: ft.NavigationBar):
    """
    Calls the control's event handler
    """
    control.on_change(
        ft.ControlEvent(
            target=control.uid,
            name="change",
            data=str(control.selected_index),
            control=control,
            page=page
        )
    )


ft.app(target=main)