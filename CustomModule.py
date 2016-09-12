from FController.Module import Module


class CustomModule(Module):
    name = ''

    def __init__(self, name):
        super(Module, self).__init__()
        self.name = name

    def die(self):
        self.services.another.say_hello('unay')
