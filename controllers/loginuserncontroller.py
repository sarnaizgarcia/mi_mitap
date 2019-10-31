from controllers.icontroller import IController
from views.mainheader import MainHeader
from views.loginusernview import UserNameLogIn


class UserNameLogInController(IController):
    def render(self):
        header = MainHeader()
        body = UserNameLogIn(header.renderbody())

        print(body.renderbody())  # imprime el body y la cabecera
        # esta acción marca la navegación
        action = input(body.rendernavigation())

        print(f'Acción seleccionada: {action}')

        return None


controller = UserNameLogInController()
