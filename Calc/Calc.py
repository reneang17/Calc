class Calc_object(object):
    def __init__(self):
        print('et print, ergo sum')

    def fizz(self):
        return 'buzz'


def add(a, b):
    checkInputs(a, b)
    return a + b

def mult(a, b):
    checkInputs(a, b)
    return a * b

def checkInputs(a, b):
    if not isinstance(a, (int)) or not isinstance(b, (int)):
        raise TypeError("Inputs must be int!")

