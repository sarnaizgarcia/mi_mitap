from controllers.icontroller import IController
from views.home import HomeView
from views.mainheader import MainHeader


class HomeController(IController):
    def render(self):
        header = MainHeader()
        body = HomeView(header.renderbody())

        print(body.renderbody())
        action = input(body.rendernavigation())

        # Print temporal
        print(f'Accion selecionada: {action}')

        # TODO Seleccionar navegación dependiendo de la accion

        return None


controller = HomeController()
