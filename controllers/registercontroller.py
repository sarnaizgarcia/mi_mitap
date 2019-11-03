from controllers.icontroller import IController
from views.mainheader import MainHeader
from views.userregisterview import UserRegister
from facade.usernamefacade import user_name_facade


class UserRegisterController(IController):
    def _navigate(self, breadcrumbs, store, user_name):
        result = ''
        if user_name_facade.validate_username(user_name):
            store.add_item('user_name', user_name)
            result = 'controllers.pswregistercontroller'
        else:
            store.add_item('error', {
                           'titulo': 'Fallo en la validacion del usuario', 'mensaje': 'El usuario es obligatorio'})
            result = 'controllers.errorcontroller'

        breadcrumbs.stack_navigation('controllers.registercontroller')
        return result

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
            result = self._navigate(breadcrumbs, store, action)
        return result


controller = UserRegisterController()
