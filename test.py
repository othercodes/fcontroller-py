#!/usr/bin/env python

from fcontroller import *

try:

    app = FController()

    app.set_module('one', 'CustomModule', ['Unay'])
    app.set_module('two', 'CustomModule', ['Leo'])
    app.set_service('another', 'CustomService')

    app.run('one.hello')
    app.run('two.hello')

except FControllerError as exception:
    print(exception.message)
