from views.iview import Iview


class UserRegister(Iview):
    def renderbody(self, variables=dict()):
        body = ''

        if self.header != None:
            body = self.header

        body += '''
        Página de registro
        '''

        return body

    def rendernavigation(self, variables=dict()):
        return'''
        Introduce tu usuario (S para salir, B para volver):
        '''
