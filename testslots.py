class Animal(object):
    __slots__ = ('colour','age','name','set_age','set_colour')

    pass

a = Animal()
a.name = 'Dog'
print(a.name)
def set_age(self,age):
    self.age = age
from types import MethodType

a.set_age = MethodType(set_age,a)
a.set_age(25)
print(a.age)

a1 = Animal()

def set_colour(self,colour):
    self.colour = colour

Animal.set_colour = MethodType(set_colour,Animal)

a.set_colour('green')
Animal.set_colour('blue')
a3 = Animal()
print(a.colour,a1.colour,a3.colour)

a3.age = 144

class Dog(Animal):
    __slots__ = ('height')
    pass

d1 = Dog()
d1.height =199
print(d1.height,d1.colour)