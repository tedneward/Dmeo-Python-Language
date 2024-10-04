#!/usr/bin/env python3

import functools

# {{## BEGIN unused ##}}
# {{## END unused ##}}

# {{## BEGIN values ##}}
sayit = print
sayit("Hello world")
print(sayit.__doc__)  # Prints the docstring for "print()"

def saySomething(mechanism, message):
    mechanism(message)

saySomething(print, "Using print")
saySomething(sayit, "Using sayit")
# {{## END values ##}}

# {{## BEGIN literals ##}}
l_sayit = lambda message: print(f"The message is {message}")
l_sayit("Hello world")

saySomething(l_sayit, "Using l_sayit")
# {{## END literals ##}}

# {{## BEGIN partial ##}}
def add(lhs : int, rhs : int) -> int:
    return lhs + rhs

print(add(5,3))     # prints "8"
add5 = functools.partial(add, 5)
print(add5(3))      # prints "8"
print(f"args for add5: {add5.args}")
print(f"keywords for add5: {add5.keywords}")
# {{## END partial ##}}

# {{## BEGIN partialmethod ##}}
from functools import partialmethod
class Cell:
    def __init__(self): self._alive = False
    @property 
    def alive(self): return self._alive
    def set_state(self, state): self._alive = bool(state)

    set_alive = partialmethod(set_state, True)
    set_dead = partialmethod(set_state, False)

c = Cell()
c.alive # prints False
c.set_alive()   # partial around set_state, above
c.alive # prints True
# {{## END partialmethod ##}}

# {{## BEGIN memoized ##}}
@functools.cache
def factorial(n):
    print(f"Calling factorial {n}")
    return n * factorial(n-1) if n else 1

print("factorial(10)")
factorial(10)      # no previously cached result, makes 11 recursive calls
print("factorial(5)")
factorial(5)       # just looks up cached value result
print("factorial(12)")
factorial(12)
# {{## END memoized ##}}

# {{## BEGIN total_ordering ##}}
from functools import total_ordering

@total_ordering
class Car():
    def __init__(self, year, make, model): 
        self.year, self.make, self.model = year, make, model

    def __eq__(self, o):
        if not isinstance(o, Car):
            return NotImplemented
        return ((self.year, self.make, self.model) == (o.year, o.make, o.model))
    
    def __lt__(self, o):
        if not isinstance(o, Car):
            return NotImplemented
        return ((self.year, self.make, self.model) < (o.year, o.make, o.model))
car1 = Car(2020, 'BMW', '530i')
car2 = Car(2020, 'BMW', '330i')
(car1 < car2), (car1 > car2) # (False, True)
# {{## END total_ordering ##}}

# {{## BEGIN generators ##}}
def generate_ints(N):
    for i in range(N):
        yield i

def generate_odds(N):
    start = 1
    while True:
        yield start
        start += 2

def is_even(x): return (x % 2) == 0
evens = list(filter(is_even, range(10)))
def is_odd(x): return (x % 2) != 0
odds = list(filter(is_odd, range(10)))
# {{## END generators ##}}

