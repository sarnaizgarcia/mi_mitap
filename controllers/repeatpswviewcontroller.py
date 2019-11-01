from getpass import getpass

from views.repeatpswview import RepeatPsw
from controllers.icontroller import IController
from views.mainheader import MainHeader


class RepeatPswController(IController):
    def render(self):
        header = MainHeader()
        body = RepeatPsw(header.renderbody())

        print(body.renderbody())
        action = getpass(body.rendernavigation())

        return None


controller = RepeatPswController()
