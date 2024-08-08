from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """ Interface method """
        pass

class Student(IPerson):

    def __init__(self):
        self.name="Basic name"


    def person_method(self):
        print("I am a student")

class Teacher(IPerson):
    def __init(self):
        self.name="Basic teacher name"


    def person_method(self):
        print("I am a teacher")

# have a factory class that builds person objects to define the object at runtime
class PersonFactory:

    @staticmethod
    def build_person(person_type: str):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("Invalid Type")
        return -1


if __name__ ==  "__main__":
    choice=input("What type of person do you want to create?")
    person = PersonFactory.build_person(choice)
    person.person_method()