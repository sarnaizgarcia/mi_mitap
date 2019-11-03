from getpass import getpass

from views.pswregisterview import PswRegister
from controllers.icontroller import IController
from views.mainheader import MainHeader
from facade.pswregisterfacade import register_psw_facade


class PswRegisterController(IController):
    def _navigate(self, breadcrumbs, store, password):
        result = ''
        if register_psw_facade.validate_pswregister(password):
            store.add_item('password', password)
            result = 'controllers.repeatpswcontroller'
        else:
            store.add_item('error', {
                           'titulo': 'Fallo en la validación del password', 'mensaje': 'El password debe tener al menos 8 caracteres'})
            result = 'controllers.errorcontroller'

        breadcrumbs.stack_navigation('controllers.pswregistercontroller')
        return result

    def render(self, breadcrumbs, store):
        result = 'controllers.repeatpswcontroller'

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
            result = self._navigate(breadcrumbs, store, action)

        return result


controller = PswRegisterController()
