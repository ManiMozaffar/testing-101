from typing import Callable


class Provider:
    @staticmethod
    def inject(container: "Container", dependency: Callable):
        container.dependencies[dependency] = dependency

    @staticmethod
    def override(
        container: "Container", dependency: Callable, new_dependency: Callable
    ):
        container.dependencies[dependency] = new_dependency


class Container:
    def __init__(self):
        self.dependencies = {}

    def get(self, dependency: Callable):
        return self.dependencies[dependency]()


def some_strings():
    return "Hello, World!"


def injected_string():
    return "Now I Am Become Death, the Destroyer of Worlds"


container = Container()
Provider.inject(container, some_strings)
print(container.dependencies)
print(container.get(some_strings))

Provider.override(container, some_strings, injected_string)
print(container.dependencies)
print(container.get(some_strings))
