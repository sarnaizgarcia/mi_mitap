from views.iview import Iview


class UserNameLogIn(Iview):
    def renderbody(self, variables=dict()):
        body = ''
        if self.header != None:
            body = self.header

        body += '''
        Login page
        '''

        return body

    def rendernavigation(self, variables=dict()):
        return '''
        Introduce tu usuario (S para salir, B para volver):
        '''
