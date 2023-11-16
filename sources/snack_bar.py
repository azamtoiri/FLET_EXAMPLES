import flet as ft


def main(page):
    page.title = "Containers with background color"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    view_hide_text = ft.Text(
        value="View",
    )

    def view_hide_password(e):
        det = text.content.password
        if det:
            text.content.password = False
            view_hide_text.value = "Hide"
        else:
            view_hide_text.value = "View"
            text.content.password = True
        text.content.update()
        view_hide_text.update()

    def password_field_in_focus(e):
        pass

    pwd_input = ft.Container(
        height=45,
        bgcolor='white',
        border_radius=10,
        # padding=20,
        content=ft.TextField(
            on_focus=password_field_in_focus,
            password=True,
            suffix=ft.Container(
                on_click=view_hide_password,
                content=view_hide_text,
            ),
            hint_text='Password',
            hint_style=ft.TextStyle(
                size=16,
                font_family='Poppins Regular',
                # color=input_hint_color,
            ),
            text_style=ft.TextStyle(
                size=16,
                font_family='Poppins Regular',
                # color=input_hint_color,
            ),
            border=ft.InputBorder.NONE,
            # content_padding=content_padding,
            # selection_color=base_green,
            # cursor_color=base_color
        )
    )

    text = ft.Container(
        height=45,
        # bgcolor="white",
        border_radius=10,
        content=ft.TextField(
            on_focus=password_field_in_focus,
            password=True,
            suffix=ft.Container(
                on_click=view_hide_password,
                content=view_hide_text,
            ),
            hint_text='Password',
            hint_style=ft.TextStyle(
                size=16,
            ),
            text_style=ft.TextStyle(
                size=16,
            ),
            # border=ft.InputBorder.NONE,
        )
    )

    text2 = ft.Container(
        height=45,
        content=ft.TextField(
            password=True,
        )
    )

    page.add(text, text2, pwd_input)
    page.update()


ft.app(target=main)
