from controllers.icontroller import IController
from views.mainheader import MainHeader
from views.userregisterview import UserRegister


class UserRegisterController(IController):
    def render(self, breadcrumbs):
        result = 'controllers.pswregistercontroller'

        header = MainHeader()
        body = UserRegister(header.renderbody())

        print(body.renderbody())

        action = input(body.rendernavigation()).upper()

        # print(f'Acción seleccionada: {action}')

        if action == 'B':
            result = breadcrumbs.unstack_navigation()
        elif action == 'S':
            result = None
        else:
            breadcrumbs.stack_navigation('controllers.registercontroller')

        return result


controller = UserRegisterController()
