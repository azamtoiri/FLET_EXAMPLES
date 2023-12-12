from flet import *

from LRSQL.flet_alchemy.login import LoginView
from LRSQL.flet_alchemy.register import RegisterView


class Application:
    def __init__(self, page: Page):
        self.page = page
        self.page.title = 'Testing DB'
        self.page.on_route_change = self.route_change

        self.login_view = LoginView()
        self.register_view = RegisterView()

        self.views = {
            self.login_view.route: self.login_view,
            self.register_view.route: self.register_view,
        }

    def route_change(self, e):
        pass
