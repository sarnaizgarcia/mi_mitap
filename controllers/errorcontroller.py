from views.error import Error
from controllers.icontroller import IController
from views.mainheader import MainHeader


class ErrorController(IController):
    def render(self, breadcrumbs, store):
        header = MainHeader()
        body = Error(header.renderbody())

        if store.exist_item('error'):
            print(body.renderbody(store.read_item('error')))
        else:
            print(body.renderbody())

        input(body.rendernavigation())

        return 'controllers.homecontroller'


controller = ErrorController()
