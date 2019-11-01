from views.iview import Iview
from string import Template


class Error(Iview):
    def renderbody(self, variables=dict()):
        body = ''
        if self.header != None:
            body = self.header

        body += '''
        Error: $titulo
        $mensaje
        '''

        if not 'titulo' in variables:
            variables.update({'titulo': 'la que has liao, pollito'})

        if not 'mensaje' in variables:
            variables.update({'mensaje': 'maloooooooo'})

        return Template(body).substitute(variables)

    def rendernavigation(self, variables=dict()):
        return '''
        Pulsa cualquier tecla para volver
        '''
