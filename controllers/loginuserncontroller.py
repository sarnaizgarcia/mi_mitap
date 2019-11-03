from controllers.icontroller import IController
from views.mainheader import MainHeader
from views.loginusernview import UserNameLogIn
from facade.usernamefacade import user_name_facade


class UserNameLogInController(IController):
    def _navigate(self, breadcrumbs, store, user_name):
        result = ''
        if user_name_facade.validate_username(user_name):
            # guarda el nombre del usuario
            store.add_item('user_name', action)
            result = 'controllers.loginpswcontroller'
        else:
            store.add_item('error', {
                           'titulo': 'Fallo en la validacion del usuario', 'mensaje': 'El usuario es obligatorio'})
            result = 'controllers.errorcontroller'

        breadcrumbs.stack_navigation(
            'controllers.loginuserncontroller')
        return result

    def render(self, breadcrumbs, store):
        result = 'controllers.loginpswcontroller'

        header = MainHeader()
        body = UserNameLogIn(header.renderbody())

        print(body.renderbody())  # imprime el body y la cabecera
        # esta acción marca la navegación
        action = input(body.rendernavigation())

        # print(f'\tAcción seleccionada: {action}')

        if action.upper() == 'B':
            result = breadcrumbs.unstack_navigation()
        elif action.upper() == 'S':
            result = None
        else:
            result = self._navigate(breadcrumbs, store, action)

        return result


controller = UserNameLogInController()
