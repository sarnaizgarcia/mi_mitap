from getpass import getpass

from views.pswregisterview import PswRegister
from controllers.icontroller import IController
from views.mainheader import MainHeader


class PswRegisterController(IController):
    def render(self, breadcrumbs):
        result = 'controllers.repeatpswcontroller'

        header = MainHeader()
        body = PswRegister(header.renderbody())

        print(body.renderbody())

        action = getpass(body.rendernavigation())

        if action == 'B' or action == 'b':
            result = breadcrumbs.unstack_navigation()
        elif action == 'S' or action == 's':
            result = None
        else:
            breadcrumbs.stack_navigation('controllers.pswregistercontroller')

        return result


controller = PswRegisterController()
