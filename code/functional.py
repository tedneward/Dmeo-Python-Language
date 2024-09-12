#!/usr/bin/env python3
import functools

# {{## BEGIN  ##}}
# {{## END  ##}}

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
