from abc import ABCMeta
from .Module import Module

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

    def run(self):
        pass

    """
    Check and build the payload call
    """

    def route(self):
        pass
