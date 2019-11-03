from views.iview import Iview
from string import Template


class Success(Iview):
    def renderbody(self, variables=dict()):
        body = ''
        if self.header != None:
            body = self.header

        if not 'title' in variables:
            variables.update(
                {'title': 'te mereces una palmadita en la espalda'})

        if not 'message' in variables:
            variables.update({'message': 'clap, clap, clap'})

        body += Template('''
        ¡Lo has conseguido!
        $title
        $message
        ''').substitute(variables)

        return Template(body).substitute(variables)

    def rendernavigation(self, variables=dict()):
        return '''
        Pulsa cualquier tecla para volver
        '''
