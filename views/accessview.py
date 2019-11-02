from views.iview import Iview
from string import Template


class Access(Iview):
    def renderbody(self, variables=dict()):
        body = ''

        if self.header != None:
            body = self.header

        body += Template('''
        Bienvenid@, $user_name
        ''').substitute(variables)

        return body

    def rendernavigation(self, variable=dict()):
        return '''
        Indica qué quieres hacer:
        '''
