from utils.breadcrumbs import BreadCrumbs

bread_crumbs = BreadCrumbs(list())

# controlador por defecto. Es con el que iniciamos la primera pantalla que pintamos
controller_path = 'controllers.homecontroller'

while controller_path != None:
    # importamos un controlador de forma dinámica (mediante una variable)
    controller_object = __import__(controller_path, fromlist=['controller'])
    controller_path = controller_object.controller.render(bread_crumbs)

print('See you later, aligator!')
