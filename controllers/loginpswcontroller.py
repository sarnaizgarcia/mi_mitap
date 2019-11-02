from getpass import getpass

from controllers.icontroller import IController
from views.mainheader import MainHeader
from views.loginpswview import PswLogIn


class PswLogInController(IController):
    def render(self, breadcrumbs):
        header = MainHeader()
        body = PswLogIn(header.renderbody())

        print(body.renderbody())
        action = getpass(body.rendernavigation())

        return None


controller = PswLogInController()
