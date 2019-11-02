from controllers.icontroller import IController
from views.mainheader import MainHeader
from views.loginusernview import UserNameLogIn


class UserNameLogInController(IController):
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
            store.add_item('user_name', action)  # guarda el nombre del usuario
            breadcrumbs.stack_navigation(
                'controllers.loginuserncontroller')

        return result


controller = UserNameLogInController()
