from controllers.icontroller import IController
from views.mainheader import MainHeader
from views.userregisterview import UserRegister


class UserRegisterController(IController):
    def render(self, breadcrumbs, store):
        result = 'controllers.pswregistercontroller'

        header = MainHeader()
        body = UserRegister(header.renderbody())

        print(body.renderbody())

        action = input(body.rendernavigation())

        # print(f'Acción seleccionada: {action}')

        if action.upper() == 'B':
            result = breadcrumbs.unstack_navigation()
        elif action.upper() == 'S':
            result = None
        else:
            store.add_item('user_name', action)
            breadcrumbs.stack_navigation('controllers.registercontroller')

        return result


controller = UserRegisterController()
