# this class can only have one single instance 
# a normal class person can have several instances, but a singleton will only have 1
from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def print_data():
        """ Implement in the child class """
        pass

class PersonSingleton(IPerson):

    # this is the single one instance that we can create here
    __instance = None

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance

    def __init__(self, name, age):
        if PersonSingleton.__instance is not None:
            raise Exception("Singleton cannot be instantiated more than once")
        else:
            self.name=name, 
            self.age=age,
            PersonSingleton.__instance=self

    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name}, Age: {PersonSingleton.__instance.age}")


p = PersonSingleton("Mike", 30)
p.print_data()
print(p)


p2 = PersonSingleton.get_instance()
p2.print_data()