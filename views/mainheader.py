from views.iview import Iview


class MainHeader(Iview):
    def renderbody(self, variables=dict()):
        body = ''

        if self.header != None:
            body = self.header

        body += '''
        >>>>========== MITAP ==========<<<<
        ___________________________________  
        '''
        return body

    def rendernavigation(self, variables=dict()):
        pass
