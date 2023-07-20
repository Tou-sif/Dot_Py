def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


if __name__ == '__main__':
    print("Hello")
    print(__name__)

# name = main only when the file itself is running,
# when a python file is immported as a library file then it is 
# implicitly executed to prevent the execution we use if clause with the dunder variable.
