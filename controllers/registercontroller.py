from controllers.icontroller import IController
from views.mainheader import MainHeader
from views.userregisterview import UserRegister


class UserRegisterController(IController):
    def render(self):
        result = None
        valid_answer = {'S': None,
                        'B': None,
                        }
        header = MainHeader()
        body = UserRegister(header.renderbody())

        print(body.renderbody())

        action = input(body.rendernavigation()).upper()

        print(f'Acción seleccionada: {action}')

        if action in valid_answer:
            result = valid_answer[action]
        else:
            result = 'controllers.pswregistercontroller'

        return result


controller = UserRegisterController()
