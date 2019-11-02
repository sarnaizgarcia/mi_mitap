from views.successview import Success
from controllers.icontroller import IController
from views.mainheader import MainHeader


class SuccessController(IController):
    def render(self, breadcrumbs, store):
        header = MainHeader()
        body = Success(header.renderbody())

        variables = dict()

        if store.exist_item('exito'):
            variables = store.read_item('exito')

        print(body.renderbody(variables))

        input(body.rendernavigation())

        return 'controllers.homecontroller'


controller = SuccessController()
