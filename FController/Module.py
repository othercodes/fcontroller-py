from abc import ABCMeta


class Module:
    __metaclass__ = ABCMeta

    services = {}

    storage = {}

    """
    Load the services into the module if they have
    not loaded already
    """

    def connect(self, services, storage):
        if len(self.services) == 0:
            self.services = services

        if len(self.storage) == 0:
            self.storage = storage
