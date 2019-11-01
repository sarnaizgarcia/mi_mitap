from views.iview import Iview


class PswRegister(Iview):
    def renderbody(self, variables=dict()):
        body = ''

        if self.header != None:
            body = self.header

        body += '''
        Página de registro\n
        Usuario creado: silvia
        '''

        return body

    def rendernavigation(self, variable=dict()):
        return '''
        Introduce tu password (S para salir, B para volver):
        '''
