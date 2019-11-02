from getpass import getpass

from views.repeatpswview import RepeatPsw
from controllers.icontroller import IController
from views.mainheader import MainHeader


class RepeatPswController(IController):
    def render(self, breadcrumbs, store):
        result = None

        if not store.exist_item('user_name') and not store.exist_item('user_password'):
            store.add_item('error', {'title': 'Acceso denegado',
                                     'message': 'No se puede acceder a la validación sin usuario y password'})
            return 'controllers.errorcontrollers'

        header = MainHeader()
        body = RepeatPsw(header.renderbody())
        variables = {'user_name': store.read_item('user_name')}

        print(body.renderbody(variables))
        action = getpass(body.rendernavigation())

        if action.upper() == 'B':
            result = breadcrumbs.unstack_navigation()
        elif action.upper() == 'S':
            result = None
        else:
            breadcrumbs.stack_navigation('controllers.repeatpswcontroller')
            store.add_item('exito', {'title': 'Registro completado',
                                     'message': 'Te has registrado con exito'})
            result = 'controllers.successcontroller'

        return result


controller = RepeatPswController()
