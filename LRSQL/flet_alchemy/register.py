from .login import LoginView


class RegisterView(LoginView):
    def __init__(self) -> None:
        super().__init__()
        self.route = '/register'
        self.title.value = 'Register'
        self.login_button, self.register_button = (
            self.register_button,
            self.login_button,
        )
        self.register_button.text = 'Sign Up'
        self.login_button.text = 'Already Have An Account? Sign in'