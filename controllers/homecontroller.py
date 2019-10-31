from controllers.icontroller import IController
from views.home import HomeView
from views.mainheader import MainHeader


class HomeController(IController):
    def render(self):
        result = None
        valid_answers = {'1': 'controllers.loginuserncontroller',
                         }
        header = MainHeader()
        body = HomeView(header.renderbody())

        print(body.renderbody())
        action = input(body.rendernavigation())

        if action in valid_answers:
            result = valid_answers[action]

        return result


controller = HomeController()
