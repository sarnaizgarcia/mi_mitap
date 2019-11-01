from controllers.icontroller import IController
from views.mainheader import MainHeader
from views.loginusernview import UserNameLogIn


class UserNameLogInController(IController):
    def render(self):
        result = None
        valid_answer = {'S': None,
                        'B': None
                        }

        header = MainHeader()
        body = UserNameLogIn(header.renderbody())

        print(body.renderbody())  # imprime el body y la cabecera
        # esta acción marca la navegación
        action = input(body.rendernavigation())

        print(f'Acción seleccionada: {action}')

        if action in valid_answer:
            result = valid_answer[action]
        else:
            result = 'controllers.loginpswviewcontroller'

        return result


controller = UserNameLogInController()
