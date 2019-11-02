from abc import ABC, abstractmethod


class IController(ABC):
    @abstractmethod
    def render(self, breadcrumbs):
        pass
