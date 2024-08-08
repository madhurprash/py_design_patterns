from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """Interface method"""
        pass

class Person(IPerson):

    def person_method(self):
        print("I am a person")


class ProxyPerson(IPerson):

    def __init__(self):
        self.person=Person()

    def person_method(self):
        print("I am the proxy functionality")
        # have a proxy to control what goes inside the method here
        # we have this proxy to add your own functionality
        # this layer of protection of abstraction gives more control and 
        # encapsulation
        self.person.person_method()


p1=Person()
p1.person_method()

p2 = ProxyPerson()
p2.person_method()