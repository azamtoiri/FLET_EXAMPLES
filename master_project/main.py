from flet import app, Page, MainAxisAlignment, CrossAxisAlignment

from utils.sign_in_form import SignInForm


def main(page: Page):
    page.window_center()
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.visible = True
    # page.window_resizable = False

    sign_in_form = SignInForm(
        logo_path='assets/Fox_Hub_logo.png'
    )

    page.add(sign_in_form)
    page.update()


if __name__ == '__main__':
    app(target=main)
