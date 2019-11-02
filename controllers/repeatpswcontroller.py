from getpass import getpass

from views.repeatpswview import RepeatPsw
from controllers.icontroller import IController
from views.mainheader import MainHeader


class RepeatPswController(IController):
    def render(self, breadcrumbs, store):
        result = None

        header = MainHeader()
        body = RepeatPsw(header.renderbody())

        print(body.renderbody())
        action = getpass(body.rendernavigation())

        if action == 'B' or action == 'b':
            result = breadcrumbs.unstack_navigation()
        elif action == 'S' or action == 's':
            result = None
        else:
            breadcrumbs.stack_navigation('controllers.repeatpswcontroller')

        return result


controller = RepeatPswController()
