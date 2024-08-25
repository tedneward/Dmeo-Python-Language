# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 14:14:47 2018

@author: Ted
"""

print(dir(__builtins__))
print(dir(abs))

def sayHello(msg = "Nothing at all"):
    "This is documentation about this sayHello function"
    print("Hello, world; Python sez", msg)

sayHello("Whitepsace is good")
sayHello()
print(sayHello.__doc__)