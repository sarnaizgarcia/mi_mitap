from controllers.icontroller import IController
from views.home import HomeView
from views.mainheader import MainHeader


class HomeController(IController):
    def render(self, breadcrumbs, store):
        result = None
        valid_answers = {'1': 'controllers.loginuserncontroller',
                         '2': 'controllers.registercontroller',
                         'S': None,
                         }
        header = MainHeader()
        body = HomeView(header.renderbody())

        print(body.renderbody())
        action = input(body.rendernavigation())

        if action.upper() in valid_answers:
            result = valid_answers[action]
        else:
            result = 'controllers.errorcontroller'

        breadcrumbs.stack_navigation('controllers.homecontroller')

        return result


controller = HomeController()
