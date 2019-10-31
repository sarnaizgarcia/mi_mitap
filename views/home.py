from views.iview import Iview


class HomeView(Iview):
    def renderbody(self, variables=dict()):
        body = ''
        if self.header != None:
            body = self.header
        body += '''
            1.- Login
            2.- Register
        '''

        return body

    def rendernavigation(self, variables=dict()):
        return '''
        Selecciona una acción (1, 2 o S para salir):
        '''
