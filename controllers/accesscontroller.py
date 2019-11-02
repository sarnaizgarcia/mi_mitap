from controllers.icontroller import IController
from views.mainheader import MainHeader
from views.accessview import Access


class AccessController(IController):
    def render(self, breadcrumbs, store):
        result = None

        # si no hay una sesión creada usuario o password han fallado
        if not store.exist_item('session_data'):
            store.add_item('error', {  # los errores se pisa, no se puede estar a la vez en varias páginas
                           'title': 'Acceso denegado',
                           'message': 'No tiene permisos para poder acceder a esta vista'})
            return 'controller.errorcontroller'

        session_data = store.read_item('session_data')
        header = MainHeader()
        body = Access(header.renderbody())
        variables = {'user_name': session_data['user_name']}

        print(body.renderbody(variables))
        action = input(body.rendernavigation())

        if action.upper() == 'B':
            result = 'controllers.homecontroller'
        elif action.upper() == 'S':
            result = None
        else:
            breadcrumbs.stack_navigation('controllers.accesscontroller')

        return result


controller = AccessController()
