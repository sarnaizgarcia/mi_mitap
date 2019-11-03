from getpass import getpass

from views.repeatpswview import RepeatPsw
from controllers.icontroller import IController
from views.mainheader import MainHeader
from facade.comparepswfacade import compare_psw


class RepeatPswController(IController):
    def _navigate(self, breadcrumbs, store, password, rep_password):
        result = ''
        if compare_psw.validate_secondpsw(password, rep_password):
            store.add_item('rep_password', rep_password)
            result = 'controllers.successcontroller'
        else:
            store.add_item('error', {
                           'titulo': 'Fallo en la validación del password', 'mensaje': 'Los passwords deben ser iguales'})
            result = 'controllers.errorcontroller'

        breadcrumbs.stack_navigation('controllers.repeatpswcontroller')
        return result

    def render(self, breadcrumbs, store):
        result = 'controllers.successcontroller'

        user_name = store.read_item('user_name')
        header = MainHeader()
        body = RepeatPsw(header.renderbody())
        variables = {'user_name': store.read_item('user_name')}

        print(body.renderbody(variables))
        action = getpass(body.rendernavigation())

        password = store.read_item('password')

        if action.upper() == 'B':
            result = breadcrumbs.unstack_navigation()
        elif action.upper() == 'S':
            result = None
        else:
            result = self._navigate(breadcrumbs, store, password, action)

        return result


controller = RepeatPswController()
