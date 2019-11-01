from getpass import getpass

from views.pswregisterview import PswRegister
from controllers.icontroller import IController
from views.mainheader import MainHeader


class PswRegisterController(IController):
    def render(self):
        result = None
        valid_answer = {'S': None,
                        'B': None,
                        }

        header = MainHeader()
        body = PswRegister(header.renderbody())

        print(body.renderbody())
        action = getpass(body.rendernavigation())

        if action in valid_answer:
            result = valid_answer[action]
        else:
            result = 'controllers.repeatpswviewcontroller'

        return result


controller = PswRegisterController()
