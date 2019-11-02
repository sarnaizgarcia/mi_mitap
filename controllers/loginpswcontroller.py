from getpass import getpass

from controllers.icontroller import IController
from views.mainheader import MainHeader
from views.loginpswview import PswLogIn


class PswLogInController(IController):
    def render(self, breadcrumbs, store):
        result = None  # más adelante se pondrá la siguiente pantalla. De momento no la tenemos, así que ponemos None

        if not store.exist_item('user_name'):
            store.add_item('error', {'title': 'Usuario no introducido',
                                     'message': 'No se ha encontrado nombre de usuario en la session'})
            return 'controllers.errorcontroller'

        user_name = store.read_item('user_name')
        header = MainHeader()
        body = PswLogIn(header.renderbody())
        variables = {'user_name': user_name}

        print(body.renderbody(variables))
        action = getpass(body.rendernavigation())

        if action == 'B' or action == 'b':
            result = breadcrumbs.unstack_navigation()
        elif action == 'S' or action == 's':
            result = None
        else:
            breadcrumbs.stack_navigation('controllers.loginpswcontroller')

        return result


controller = PswLogInController()
