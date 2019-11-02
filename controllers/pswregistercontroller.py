from getpass import getpass

from views.pswregisterview import PswRegister
from controllers.icontroller import IController
from views.mainheader import MainHeader


class PswRegisterController(IController):
    def render(self, breadcrumbs, store):
        result = 'controllers.repeatpswcontroller'

        if not store.exist_item('user_name'):
            store.add_item('error', {'title': 'Usuario incorrecto',
                                     'message': 'No se ha encontrado el nombre de usuario'})

        user_name = store.read_item('user_name')
        header = MainHeader()
        body = PswRegister(header.renderbody())
        variables = {'user_name': user_name}

        print(body.renderbody(variables))
        action = getpass(body.rendernavigation())

        if action.upper() == 'B':
            result = breadcrumbs.unstack_navigation()
        elif action.upper() == 'S':
            result = None
        else:
            breadcrumbs.stack_navigation('controllers.pswregistercontroller')
            store.add_item('user_password', action)

        return result


controller = PswRegisterController()
