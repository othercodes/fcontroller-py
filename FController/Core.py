import re
from abc import ABCMeta
from .Module import Module
from .FControllerError import FControllerError

"""
Core of the controller
author Unay Santisteban <usantisteban@othercode.es>
"""


class Core(object):
    __metaclass__ = ABCMeta

    VERSION = '1.0.0'

    """
    The registry of all modules
    """
    modules = {}

    """
    The registry of all services
    """
    services = {}

    """
    Shared store space
    """
    storage = {}

    """
    Register a new module instance into the registry
    """

    def register_module(self, name, module):
        if name not in self.modules and isinstance(module, Module):
            module.connect(self.services, self.storage)
            self.modules[name] = module
            return True
        return False

    """
    Delete a module instance
    """

    def unregister_module(self, name):
        if name in self.modules:
            del self.modules[name]
            return True
        return False

    """
    Register and instantiate a new service
    """

    def register_service(self, name, service):
        if name not in self.services:
            self.services[name] = service
            return True
        return False

    """
    Delete a service
    """

    def unregister_service(self, name):
        if name in self.services:
            del self.services[name]
            return True
        return False

    """
    Perform the main call of the module method
    """

    def run(self, path, data=[]):
        path = self.__route(path)
        print(path)
        # getattr(self.modules[path.module], path.operation)(*data)

    """
    Check and build the payload call
    """

    def __route(self, path):
        if re.compile('^[a-zA-Z0-9_]+\.[a-zA-Z0-9_]+$').search(path) is None:
            raise FControllerError('Incorrect module call pattern')

        call_path = path.split(".")

        if call_path[0] not in self.modules:
            raise FControllerError('Module instance not found')

        if call_path[1] not in dir(self.modules[call_path[0]]):
            raise FControllerError('Module method requested is not available')

        return {'name': call_path[0], 'operation': call_path[1]}
