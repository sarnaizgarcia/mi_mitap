from getpass import getpass

from controllers.icontroller import IController
from views.mainheader import MainHeader
from views.loginpswview import PswLogIn
from facade.pswloginfacade import login_psw_facade


class PswLogInController(IController):
    def _navigate(self, breadcrumbs, store, password):
        result = ''
        if login_psw_facade.validate_loginpsw(password):
            store.add_item('session_data', {
                           'user_name': store.read_item('user_name')})
            result = 'controllers.accesscontroller'
        else:
            store.add_item('error', {
                           'titulo': 'Fallo en la validación del password', 'mensaje': 'El password es obligatorio'})
            result = 'controllers.errorcontroller'

        breadcrumbs.stack_navigation('controllers.loginpswcontroller')
        return result

    def render(self, breadcrumbs, store):
        result = 'controllers.accesscontroller'

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
            result = self._navigate(breadcrumbs, store, action)

        return result


controller = PswLogInController()
