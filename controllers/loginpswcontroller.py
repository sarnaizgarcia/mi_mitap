from getpass import getpass

from controllers.icontroller import IController
from views.mainheader import MainHeader
from views.loginpswview import PswLogIn


class PswLogInController(IController):
    def render(self, breadcrumbs, store):
        result = 'controllers.accesscontroller'

        if not store.exist_item('user_name'):
            store.add_item('error', {'title': 'Usuario no introducido',
                                     'message': 'No se ha encontrado nombre de usuario en la sessión'})
            return 'controllers.errorcontroller'

        user_name = store.read_item('user_name')
        header = MainHeader()
        body = PswLogIn(header.renderbody())
        variables = {'user_name': user_name}  # para pasarlo a la vista

        print(body.renderbody(variables))
        action = getpass(body.rendernavigation())

        if action.upper() == 'B':
            result = breadcrumbs.unstack_navigation()
        elif action.upper() == 'S':
            result = None
        else:
            breadcrumbs.stack_navigation('controllers.loginpswcontroller')
            store.add_item('session_data', {'user_name': user_name})

        return result


controller = PswLogInController()
