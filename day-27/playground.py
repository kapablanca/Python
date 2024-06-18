def add(*args):
    number = 0
    for n in args:
        number += n
    return number

print(add(25,18,2))

def calculate(n, **kwargs):
    print(kwargs)
   #for key, value in kwargs.items():
   #print(key)
   #print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]



calculate(add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="Nissan", model="GTR")
print((my_car.model))