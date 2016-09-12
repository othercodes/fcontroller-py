from var_dump import var_dump
from CustomService import CustomService
from FController.FControllerError import FControllerError

from FController import FController
from CustomModule import CustomModule

try:

    app = FController()
    app.register_module('one', CustomModule('Rick'))
    app.register_module('two', CustomModule('Morty'))
    app.register_service('another', CustomService())
    app.run('one.say_hello')

    var_dump(app.modules)

except FControllerError as exception:
    print(exception.message)
