#!/usr/bin/env python3

# Python flow control

## {{## BEGIN if ##}}
age = 45
if age > 50:
    print("You old!")
elif age < 18:
    print("Juvie!")
else:
    print("You not old!")

insult = "Boomer!" if age > 50 else "Millennial!"
## {{## END if ##}}

status = 400
## {{## BEGIN match ##}}
http_message = ""
match status:
    case 400:
        http_message = "Bad request"
    case 404:
        http_message = "Not found"
    case 418:
        http_message = "I'm a teapot"
    case _:
        http_message = "Something's wrong with the internet"
## {{## END match ##}}

point = (0, 0)
## {{## BEGIN tuple-match ##}}
# point is tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y) if x == y:
        print(f"Y=X at {x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
## {{## END tuple-match ##}}

## {{## BEGIN while ##}}
x = 3
while x > 0:
    print("x is still more than 0")
    x = x -1
else:
    print("x is now " + str(x))
## {{## END while ##}}

## {{## BEGIN for ##}}    
for c in range(10):
    print(c)
else:
    print("Can we see c?", c)
print("Can we still see c?", c)

message = "Python is interesting"
for ch in message:
    print(ch)
    
attendees = ["Marcel", "Roy", "Jeremy"]
for at in attendees:
    print(at)

my_first_tuple = "Ted", "Neward", 47
for t in my_first_tuple:
    print(t)
## {{## END for ##}}

## {{## BEGIN exceptions ##}}
try:
    bad_div = 1/0
except ZeroDivisionError:
    print("Silly boy; you can't do that")
else:
    print("Else!")
finally:
    print("Finally!")
    
try:
    print("In a new try block")
    raise Exception()
except Exception:
    print("We just raised this!")
print("Onwards we execute...")
## {{## END exceptions ##}}

## {{## BEGIN generators ##}}
def names():
    yield "Ted"
    yield "Brian"
    yield "Brent"

for n in names():
    print(n)
## {{## END generators ##}}


## {{## BEGIN switchdict ##}}
import operator as op
calculator = { '+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv }

left = int(input())
op = input()
right = int(input())
print(calculator[op](left, right))
## {{## END switchdict ##}}
