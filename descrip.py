class Descriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        print(f"{self.name}:__get__")

    def __set__(self, instance, value):
        print(f"{self.name}:__set__ {value}")

    def __delete__(self, instance):
        print(f"{self.name}:__delete__")
