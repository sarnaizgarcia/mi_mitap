from views.iview import Iview
from string import Template


class Success(Iview):
    def renderbody(self, variables=dict()):
        body = ''
        if self.header != None:
            body = self.header

        body += Template('''
        ¡Lo has conseguido!
        $titulo
        $mensaje
        ''').substitute(variables)

        if not 'titulo' in variables:
            variables.update(
                {'titulo': 'te mereces una palmadita en la espalda'})

        if not 'mensaje' in variables:
            variables.update({'mensaje': 'clap, clap, clap'})

        return Template(body).substitute(variables)

    def rendernavigation(self, variables=dict()):
        return '''
        Pulsa cualquier tecla para volver
        '''
