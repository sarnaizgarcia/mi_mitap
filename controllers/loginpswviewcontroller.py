from controllers.icontroller import IController
from views.mainheader import MainHeader
from views.loginpswview import PswLogIn


class PswLogInController(IController):
    def render(self):
        header = MainHeader()
        body = PswLogIn(header.renderbody())

        print(body.renderbody())
        action = input(body.rendernavigation())

        return None


controller = PswLogInController()
