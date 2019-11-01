from views.iview import Iview


class PswLogIn(Iview):
    def renderbody(self, variables=dict()):
        body = ''
        if self.header != None:
            body = self.header

        body += '''
        Login page\n\n
        Usuario introducido: silvia
        '''

        return body

    def rendernavigation(self, variables=dict()):
        return '''
        Introduce tu password (S para salir, B para volver):
        '''
