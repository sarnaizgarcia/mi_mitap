from abc import ABC, abstractmethod


class Iview(ABC):
    def __init__(self, header=None):
        self.header = header

    @abstractmethod  # renderiza el texto plano de la pantalla
    def renderbody(self, variables=dict()):
        pass

    @abstractmethod
    # renderiza el input que nos lleva de una 'vista' a otra
    def rendernavigation(self, variables=dict()):
        pass
