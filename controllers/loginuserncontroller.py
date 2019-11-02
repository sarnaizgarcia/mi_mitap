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
        action = input(body.rendernavigation()).upper()

        # print(f'\tAcción seleccionada: {action}')

        if action == 'B':
            result = breadcrumbs.unstack_navigation()
        elif action == 'S':
            result = None
        else:
            store.add_item('user_name', action)
            breadcrumbs.stack_navigation(
                'controllers.loginuserncontroller')

        return result


controller = UserNameLogInController()
