from views.successview import Success
from controllers.icontroller import IController
from views.mainheader import MainHeader


class SuccessController(IController):
    def render(self, breadcrumbs, store):
        header = MainHeader()
        body = Success(header.renderbody())

        if store.exist_item('éxito'):
            print(body.renderbody(store.read_item('éxito')))
        else:
            print(body.renderbody())

        input(body.rendernavigation())

        return 'controllers.homecontroller'


controller = SuccessController()
