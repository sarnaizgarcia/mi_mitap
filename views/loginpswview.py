from views.iview import Iview
from string import Template


class PswLogIn(Iview):
    def renderbody(self, variables=dict()):
        body = ''
        if self.header != None:
            body = self.header

        body += Template('''
        Login page\n
        Usuario introducido: $user_name
        ''').substitute(variables)

        return body

    def rendernavigation(self, variables=dict()):
        return '''
        Introduce tu password (S para salir, B para volver):
        '''
