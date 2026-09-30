def add(a, b):
    return a + b


result = add(10, 20)

print("Result:", result)

def greet(name="Ujjwal"):
    print("Hello", name)


greet()
greet("Rahul")

def logger(func):

    def wrapper():
        print("Function started")

        func()

        print("Function completed")

    return wrapper


@logger
def hello():
    print("Hello, Python!")


hello()