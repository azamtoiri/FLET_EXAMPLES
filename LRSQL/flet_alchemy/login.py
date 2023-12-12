import flet as ft


class LoginView(ft.View):
    def __init__(self) -> None:
        super().__init__()
        self.route = '/login'
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.title = ft.Text()
        self.title.value = 'Login'
        self.title.style = ft.TextThemeStyle.DISPLAY_MEDIUM
        self.title.text_align = ft.TextAlign.CENTER
        self.title.expand = True

        self.username_field = ft.TextField()
        self.username_field.label = 'Username'
        self.username_field.expand = True

        self.password_field = ft.TextField()
        self.password_field.label = 'Password'
        self.password_field.password = True
        self.password_field.can_reveal_password = True
        self.password_field.expand = True

        self.login_button = ft.OutlinedButton()
        self.login_button.text = 'Sign In'
        self.login_button.icon = ft.icons.LOGIN
        self.login_button.expand = True

        self.register_button = ft.TextButton()
        self.register_button.text = "Don' Have An Account? Sign Up"
        self.register_button.icon = ft.icons.ARROW_FORWARD
        self.register_button.expand = True

        content = ft.Column()
        content.width = 400
        content.alignment = ft.MainAxisAlignment.CENTER
        content.controls.append(ft.Row([self.title]))
        content.controls.append(ft.Row([self.username_field]))
        content.controls.append(ft.Row([self.password_field]))
        content.controls.append(ft.Row([self.login_button]))
        content.controls.append(ft.Row([self.register_button]))

        container = ft.Container()
        container.content = content
        container.border = ft.border.all(1, ft.colors.TRANSPARENT)
        container.expand = True
        self.controls.append(container)
