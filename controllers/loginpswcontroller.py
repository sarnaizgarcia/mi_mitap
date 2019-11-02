from getpass import getpass

from controllers.icontroller import IController
from views.mainheader import MainHeader
from views.loginpswview import PswLogIn


class PswLogInController(IController):
    def render(self, breadcrumbs):
        result = None  # más adelante se pondrá la siguiente pantalla. De momento no la tenemos, así que ponemos None

        header = MainHeader()
        body = PswLogIn(header.renderbody())

        print(body.renderbody())
        action = getpass(body.rendernavigation())

        if action == 'B' or action == 'b':
            result = breadcrumbs.unstack_navigation()
        elif action == 'S' or action == 's':
            result = None
        else:
            breadcrumbs.stack_navigation('controllers.loginpswcontroller')

        return result


controller = PswLogInController()
