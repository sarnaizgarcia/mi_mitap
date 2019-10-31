import json

# controlador por defecto. Es con el que iniciamos la primera pantalla que pintamos
controller_path = 'controllers.homecontroller'

while controller_path != None:
    # importamos un controlador,
    controller_object = __import__(controller_path, fromlist=['controller'])
    controller_path = controller_object.controller.render()

print('See you later, aligator!')
