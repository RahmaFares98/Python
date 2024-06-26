
local_val = "magical unicorns"

def square(x):
    return x * x

class User:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return "hello"

if __name__ == "__main__":
    # Test the functionality only if this file is executed directly
    print(square(5))
    user = User("Anna")
    print(user.name)
    print(user.say_hello())
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)
