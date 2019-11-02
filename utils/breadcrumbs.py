# Clase que permita el acceso a estuctura de pila


class BreadCrumbs(object):
    def __init__(self, navigations):
        self.navigations = list()

    def stack_navigation(self, controller):
        # controller se coloca en la primera posición de la lista
        if not self.navigations:
            self.navigations.insert(0, controller)
        elif self.navigations and self.navigations[0] != controller:
            self.navigations.insert(0, controller)

    def unstack_navigation(self):
        # coge el primer elemento de la lista, lo borra de la lista y lo devuelve
        element = self.navigations[0]
        self.navigations.pop(0)
        return element
