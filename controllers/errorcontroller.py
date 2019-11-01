from views.error import Error
from controllers.icontroller import IController
from views.mainheader import MainHeader


class ErrorController(IController):
    def render(self):
        header = MainHeader()
        body = Error(header.renderbody())

        print(body.renderbody())

        input(body.rendernavigation())

        return 'controllers.homecontroller'


controller = ErrorController()
