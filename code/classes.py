#!/usr/bin/env python3

# Python classes

# {{## BEGIN definition ##}}
class Person:
    """Someday this class will represent a human being"""

    # count is a "class variable" (static)
    count = 0

    # sayHello is a "class method" (static)    
    def sayHello():
        print("Hello, world!")

print(Person.count)
Person.sayHello()
# {{## END definition ##}}

# {{## BEGIN initializer ##}}
class Person:
    def __init__(self, fn, ln, a):
        self.firstName = fn
        self.lastName = ln
        self.age = a
    
    def code(self):
        print(self.firstName + " is coding, coding, coding...")

ted = Person("Ted", "Neward", 48)
ted.code()
# {{## END initializer ##}}

# {{## BEGIN property ##}}
class Monster:
    def __init__(self, name):
        self._name = name
    
    def getname(self):
        return self._name
    
    def setname(self, value):
        self._name = value

    def delname(self):
        del self._name

    name = property(getname, setname, delname, "The Monster's name")

orc = Monster("Orc")
print("The " + orc.name + " attacks you!")
# {{## END property ##}}

# {{## BEGIN decorator-property ##}}
class Item:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

magicSword = Item("Sword +1")
print(magicSword.name + " is such a boring name")
magicSword.name = "Sting"  # Much better
# {{## END decorator-property ##}}

# {{## BEGIN inheritance ##}}
class Student(Person):
    def study(self, subject):
        print(self.firstName + " is studying " + subject)
# {{## END inheritance ##}}

# {{## BEGIN manipulation ##}}
intern = Person("Joe", "Intern", 20)
intern.code()
    # "Joe is coding, coding, coding..."

print(dir(intern))
    # (Prints out a lot of methods, most of which we didn't define)

internCodeFunction = intern.code
internCodeFunction()
    # "Joe is coding, coding, coding..."
# {{## END manipulation ##}}

# {{## BEGIN conventions ##}}
class Example:
    def __init__(self):
        print("Object constructor")
    def __del__(self):
        print("Object finalizer/destructor")
    def __repr__(self):
        print("Stringified representation of this object")
    def __eq__(self, other):
        print("Does this == other?")
        # See also __lt__, __le__, __gt__, __ge__, __ne__
    def __hash__(self):
        print("Generate a hash code for this object")
    def __bool__(self):
        print("returns True or False")
# {{## END conventions ##}}

# {{## BEGIN metaprogramming ##}}
Person.listLanguages = lambda: "There is only Python"
print(Person.listLanguages())
Person.codeBetter = lambda self: self.firstName + " is coding in Python"
print(ted.codeBetter())
# {{## END metaprogramming ##}}
