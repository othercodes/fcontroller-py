#!/usr/bin/env python

from fcontroller.Module import Module


class CustomModule(Module):

    def __init__(self, name):
        self.name = name

    def hello(self):
        self.another.say_hello(self.name)


