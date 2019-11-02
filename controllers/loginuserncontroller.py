from controllers.icontroller import IController
from views.mainheader import MainHeader
from views.loginusernview import UserNameLogIn


class UserNameLogInController(IController):
    def render(self, breadcrumbs):
        result = None
        valid_answer = {'S': None,
                        }

        header = MainHeader()
        body = UserNameLogIn(header.renderbody())

        print(body.renderbody())  # imprime el body y la cabecera
        # esta acción marca la navegación
        action = input(body.rendernavigation()).upper()

        print(f'Acción seleccionada: {action}')

        if action == 'B':
            result = breadcrumbs.unstack_navigation()
        if action in valid_answer:
            result = valid_answer[action]
            breadcrumbs.stack_navigation('controllers.loginuserncontroller')

        return result


controller = UserNameLogInController()
