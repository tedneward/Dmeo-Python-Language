#!/usr/bin/env python3

# Python functions

# {{## BEGIN  ##}}
# {{## END  ##}}

# {{## BEGIN examples ##}}
print("Hello, Python!")
print(dir(__builtins__))
# {{## END examples ##}}

# {{## BEGIN definition ##}}
def sayHowdy():
    """This function says howdy and returns the same"""
    print("Howdy!")
    return "I said howdy"

response = sayHowdy()
print(response)             # "I said howdy"
print(sayHowdy.__doc__)     # "This function says..."
# {{## END definition ##}}

# {{## BEGIN typed_definition ##}}
def add(lhs : int, rhs : int) -> int:
    return lhs + rhs
def concat(str1 : str, str2 : str) -> str:
    return str1 + str2

print(add(2, 3))            # 5
print(add('1', '2'))        # 12
print(concat(1, 2))         # 3
print(concat('1', '2'))     # 12
# {{## END typed_definition ##}}

# {{## BEGIN default-args ##}}
def sayGoodMorning(language="english"):
    if (language == "english"):
        return "Good morning!"
    else:
        return f"Sorry, I don't speak {language}"

print(sayGoodMorning())
print(sayGoodMorning("french"))
# {{## END default-args ##}}

# {{## BEGIN keyword-args ##}}
def saySomething(message="Hello", language="English", times=1):
    """Prints a message in a language a number of times"""
    for x in range(times):
        print(message + " (in " + language + ")")

saySomething(language="German", times=3, message="Good Morning")
# {{## END keyword-args ##}}

# {{## BEGIN arb-arg-lists ##}}
def myPrint(prefix, *rest):
    message = prefix
    for r in rest:
        message += " " + r
    print(message)

myPrint("Salutations")
myPrint("Salutations", "planet")
# {{## END arb-arg-lists ##}}

# {{## BEGIN formal-params ##}}
def speak(**args):
    print(args)
    for key, value in args.items():
        print("argument " + str(key) + " = " + str(value))

speak(one="1", two="2", three="3")
# {{## END formal-params ##}}

# {{## BEGIN fn-literals ##}}
fn_lit = saySomething
fn_lit("Hello", "English", 2)
# {{## END fn-literals ##}}

# {{## BEGIN lambdas ##}}
messages = ["Hello", "Guten morgen", "Bonjour"]
def capIt(x):
    return x.upper()
print(capIt("hello"))   # "HELLO"
up_messages = map(capIt, messages)    # "HELLO", "GUTEN MORGEN", "BONJOUR"
up_messages2 = map(lambda x: x.upper, messages) # same as previous

add_one = lambda x: x+1     # same as def add_one(x): return x+1
result = (lambda x: x+1)(2) # 3
# {{## END lambdas ##}}

# {{## BEGIN generators ##}}
def generator_function():
    for i in range(10):
        yield i
for i in generator_function():
    print(i)

def fibonacci(n):
    a = b = 1
    for i in range(n):
        yield a
        a,b = b, a+b
# {{## END generators ##}}

# {{## BEGIN comprehensions ##}}
squares1 = []
for x in range(10):
    squares1.append(x**2)
# or...    
squares2 = list(map(lambda x: x**2, range(10)))
# or...
squares3 = [x**2 for x in range(10)]
# {{## END comprehensions ##}}

# {{## BEGIN comprehensions-1 ##}}
x = [2, 3, 4, 5, 6]
y = []
for v in x :
    y += [v * 5]        # y == [10, 15, 20, 25, 30]

y2 = map(lambda v : v * 5, x)

y3 = [v * 5 for v in x] # y3 == [10, 15, 20, 25, 30]
# {{## END comprehensions-1 ##}}

# {{## BEGIN comprehensions-2 ##}}
for v in x :
        if v % 2 :
            y += [v * 5]

y2 = map(lambda v : v * 5, filter(lambda u : u % 2, x))

y3 = [v * 5 for v in x if v % 2]
# {{## END comprehensions-2 ##}}

# {{## BEGIN globals ##}}
player = "Fred"

def doSomething():
    #global player  # without this, it's an error
        # "UnboundLocalError: local variable 'player' referenced before assignment"
    player = player + " and Jed"
    print(player)

doSomething()
# {{## END globals ##}}
