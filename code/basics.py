#!/usr/bin/env python3

# Python basics

## {{## BEGIN variables ##}}
num = 5
message = "This is a string"
this_is_a_really_long_variable = 0
x,y = 0,0
#uninitialized_variable  # error!
## {{## END variables ##}}

## {{## BEGIN walrus ##}}
assignment = (truth := True)
print(assignment)
## {{## END walrus ##}}

## {{## BEGIN tuples ##}}
ted = "Ted", "Neward", 46
print(ted)                 # ("Ted", "Neward", 46)
charlotte = ("Charlotte", "Neward", 39)
first, last, age = ted
print(first)               # "Ted"
## {{## END tuples ##}}


## {{## BEGIN numbers ##}}
div1 = 5 / 2      # 2.5
div2 = 5 // 2     # 2
square = 2 ** 2   # 4
## {{## END numbers ##}}


## {{## BEGIN strings ##}}
str1 = "hello"
str2 = 'hello'

str3 = r"Long live metal \m/"

str4 = f"{str1}. I would like to say {str3}"

str5 = """
This is a here-doc. It can span lines.
It will continue going until we run into
the triple-quote again. It is often used
for documentation and simple formatting
purposes.
"""

str6 = "This" "is" "several" "strings"

str7 = str4[6:8]  # "is"
## {{## END strings ##}}

class User:
  def __init__(self):
    self.name = "Fred Flintstone"
    self.age = 47
user = User()

## {{## BEGIN format ##}}
# assume 'user' points to a user object
output = 'Name: {user.name}, Age: {user.age}'.format(user=user)
## {{## END format ##}}


## {{## BEGIN lists ##}}
list1 = [1, 2, 3, 4, 5]
list2 = [1, "two", 3.0]
list3 = list1 + list2       # [1, 2, 3, 4, 5, 1, "two", 3.0]
firstlistelement = list1[0] # 1
lastlistelement = list1[-1] # 5
## {{## END lists ##}}
print(list3)
print(firstlistelement)     # "1"
print(lastlistelement)      # "5"

## {{## BEGIN sets ##}}
set1 = {1, 2, 3, 4, 5}
set2 = {1, 1, 2, 2, 3, 3, 4, 4}
print(set2)                 # "{1, 2, 3, 4}"

set3 = {2, 4, 6}
set4 = {1, 4, 9, 16}
print(set3 & set4)          # "{4}" 
print(set3 - set4)          # "{2, 6}"
print(set3 | set4)          # "{16, 1, 2, 4, 6, 9}"
## {{## END sets ##}}

## {{## BEGIN dicts ##}}
dict1 = { "captain":"Antilles" }
dict1["admiral"] = "Ackbar"
k = dict1.keys()
v = dict1.values()
kv = dict1.items()

another_dict = dict(name="Ted",age=47)
print(another_dict)   # {'name':'Ted','age':47}
## {{## END dicts ##}}
