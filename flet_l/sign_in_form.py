import asyncio

import flet as ft
import flet_material as fm

PRIMARY = ft.colors.TEAL

fm.Theme.set_theme(theme=PRIMARY)

# user login and password
dummy_user_list: list = [["dummy@gmail.com", 12341234]]


class CustomInputField(ft.UserControl):
    def __init__(self, password: bool, title: str):
        self.view_hide_text = ft.Text(
            value="View",
        )

        self.error = ft.Text(
            value='Incorrect login or password',
            color=ft.colors.RED_300,
            visible=False,
        )

        self.input_box: ft.Container = ft.Container(
            expand=True,
            content=ft.TextField(
                height=50,
                # few UI properties for the text-fields hard@
                border_color=ft.colors.PRIMARY,
                border_width=1,
                cursor_width=0.5,
                cursor_color=ft.colors.WHITE10,
                color=ft.colors.WHITE,
                text_size=13,

                # bgcolor as per the theme
                bgcolor=fm.Theme.bgcolor,
                password=password,
                on_focus=self.focus_shadow,
                on_blur=self.blur_shadow,
                on_change=self.set_loader_animation,
                suffix=ft.Container(
                    content=self.view_hide_text,
                    on_click=self.view_hide_password,
                )
            ),
            animate=ft.Animation(300, ft.animation.AnimationCurve.EASE),
            shadow=None,
        )

        self.loader: ft.ProgressBar = ft.ProgressBar(
            value=0,
            bar_height=1.25,
            color=PRIMARY,
            bgcolor=ft.colors.TRANSPARENT,
        )

        self.status: fm.CheckBox = fm.CheckBox(
            shape="circle",
            value=False,
            disabled=True,
            offset=ft.Offset(1, 0),
            bottom=0,
            right=1,
            top=1,
            animate_opacity=ft.Animation(200, ft.animation.AnimationCurve.LINEAR),
            animate_offset=ft.Animation(300, ft.animation.AnimationCurve.EASE),
            opacity=0,
        )

        self.object = self.create_input(title)

        super().__init__()

    def view_hide_password(self, e):
        det = self.input_box.content.password
        if det:
            self.input_box.content.password = False
            self.view_hide_text.value = "Hide"
        else:
            self.view_hide_text.value = "View"
            self.input_box.content.password = True
        self.update()

    async def set_ok(self):
        self.view_hide_text.value = ""

        self.loader.value = 0
        self.loader.update()

        self.status.offset = ft.Offset(-0.5, 0)
        self.status.opacity = 1
        self.update()
        await asyncio.sleep(1)

        self.status.content.value = True
        self.status.animate_checkbox(e=None)
        self.status.update()

    async def set_fail(self):
        self.loader.value = 0
        self.loader.update()

        self.input_box.content.border_color = ft.colors.with_opacity(0.5, 'red')
        self.error.visible = True
        await asyncio.sleep(1)
        self.update()

    def set_loader_animation(self, e):
        # function starts the loader if the text field lengths ore not 0
        if len(self.input_box.content.value) != 0:
            self.loader.value = None
        else:
            self.loader.value = 0

        self.loader.update()

    def focus_shadow(self, e):
        """Focus shadow when focusing"""
        self.error.visible = False
        self.input_box.content.border_color = ft.colors.WHITE
        self.input_box.border_color = PRIMARY
        self.input_box.shadow = ft.BoxShadow(
            spread_radius=6,
            blur_radius=8,
            color=ft.colors.with_opacity(0.25, ft.colors.BLACK),
            offset=ft.Offset(4, 4)
        )
        self.update()
        self.set_loader_animation(e=None)

    def blur_shadow(self, e):
        """ Blur when the textfield loses focus"""
        self.input_box.shadow = None
        self.input_box.content.border_color = ft.colors.WHITE
        self.update()
        self.set_loader_animation(e=None)

    def create_input(self, title):
        return ft.Column(
            spacing=5,
            controls=[
                ft.Text(title, size=11, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                ft.Stack(
                    controls=[
                        self.input_box,
                        self.status,
                    ],
                ),
                self.loader,
                self.error,
            ],
        )

    def build(self):
        return self.object


# Mian form class: stores the major instances
class MainFormUI(ft.UserControl):
    def __init__(self):
        self.email = CustomInputField(False, "Email or Login ")
        self.password = CustomInputField(True, "Password")

        # create crutch for show and hide password
        self.email.view_hide_text.visible = True
        self.email.view_hide_text.value = ""

        self.submit = fm.Buttons(
            width=400,
            height=45,
            title="Submit",
            on_click=lambda e: asyncio.run(self.validate_entries(e))
        )
        super().__init__()

    async def validate_entries(self, e):
        if self.email.input_box.content.value is None:
            await e.control.page.update_async()

        email_value = self.email.input_box.content.value
        password_value = self.password.input_box.content.value

        for user, password in dummy_user_list:
            if email_value == user and password_value == str(password):
                await asyncio.sleep(0.5)
                await self.email.set_ok()
                await asyncio.sleep(1)
                await self.password.set_ok()
                self.update()
            else:
                await self.email.set_fail()
                await self.password.set_fail()
                self.update()

    def build(self):
        return ft.Container(
            width=450, height=550,
            bgcolor=ft.colors.with_opacity(0.01, "white"),
            border_radius=10,
            padding=40,
            content=ft.Column(
                horizontal_alignment=ft.alignment.center,
                alignment=ft.alignment.center,
                controls=[
                    ft.Text(
                        "Validating Signin Form - Flet",
                        size=21,
                        weight=ft.FontWeight.W_800,
                        color=ft.colors.with_opacity(0.85, "white")
                    ),
                    ft.Divider(height=25, color=ft.colors.TRANSPARENT),
                    self.email,
                    ft.Divider(height=5, color=ft.colors.TRANSPARENT),
                    self.password,
                    ft.Divider(height=25, color=ft.colors.TRANSPARENT),
                    self.submit,
                ],
            ),
        )


def main(page: ft.Page):
    page.bgcolor = fm.Theme.bgcolor

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    form = MainFormUI()
    page.add(form)
    page.update()


# TODO: Notification for incorrect password or email

if __name__ == '__main__':
    ft.app(target=main)
