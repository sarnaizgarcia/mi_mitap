from views.iview import Iview
from string import Template


class RepeatPsw(Iview):
    def renderbody(self, variables=dict()):
        body = ''

        if self.header != None:
            body = self.header

        body += Template('''
        Página de registro\n
        Usuario creado: $user_name
        ''').substitute(variables)

        return body

    def rendernavigation(self, variable=dict()):
        return '''
        Vuelve a introducir tu password (S para salir, B para volver):
        '''
