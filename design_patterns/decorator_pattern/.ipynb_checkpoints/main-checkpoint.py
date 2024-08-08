# decorators help wrap a functionality around a function.
# basic idea: they add a certain functionality around a function

def mydecorator(function):

    def wrapper(*args, **kwargs):
        # some functionality here
        return_value = function(*args, **kwargs)
        print("I am decorating your function")
        return return_value

    return wrapper

@mydecorator
def hello_person(person):
    print(f"hello {person}")
    return f"hello {person}"


# mydecorator(hello_world)()
# this gives:
# I am decorating your function
# hello world

# hello_world()

hello_person("mike")