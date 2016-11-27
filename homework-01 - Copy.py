"""
Name: Darien Cortez
Email: darien.cortez@gmail.com
Assignment: Homework 1 - Lists and Dictionaries
Due: 19 Sep @ 1:00 p.m.
"""

# A:  What would Python print?

a = [1, 5, 4, 2, 3] 
print(a[0], a[-1])
# Prints: 1 3

a[4] = a[2] + a[-2]
print(a)
# Prints: [1, 5, 4, 2, 6]

print(len(a))
# Prints: 5

print(4 in a)
# Prints: True

a[1] = [a[1], a[0]]
print(a)
# Prints: [1, [5, 1], 4, 2, 6]

#B:  Function that removes all instances of an element from a list.

x = [3, 1, 2, 1, 5, 1, 1, 7]
def remove_all(e, lst):
    for el in lst:
            lst.remove(e)
    return (lst)

remove_all(1,x)

# C:  Function that takes in two values, x and y, and a list, and adds as many y's to the end of the list as there are x's.

lst = [1, 2, 4, 2, 1]
def add_this_many(x, y, lst):
    for el in lst:
        if (lst[x]):
            lst.append(y)
    return(lst)

add_this_many(1, 5, lst)

# D:  What would Python print?

a = [3, 1, 4, 2, 5, 3]
print(a[:4])
# Prints: [3, 1, 4, 2]

print(a)
# Prints: [3, 1, 4, 2, 5, 3]

print(a[1::2])
# Prints: [1, 2, 3]

print(a[:])
# Prints: [3, 1, 4, 2, 5, 3]

print(a[4:2])
# Prints: []

print(a[1:-2])
# Prints: [1, 4, 2]

print(a[::-1])
# Prints: [3, 5, 2, 4, 1, 3]

# E:  Reverse Python list

x = [3, 2, 4, 5, 1] 
def reverse(lst):
    for el in lst:
        lst = lst[::-1]
    return (lst)

reverse(x)

# F.  Write a function that rotates the elements of a list to the right by  k . Elements should not ”fall off”; they should wrap around the beginning of the list.  rotate  should return a new list. To make a list of  n   0's ,you can do this:  [0] * n 

x = [1, 2, 3, 4, 5]
def rotate(lst, k):
    return (lst[-k:] + lst[:-k])

rotate(x, 3)    

# H:  Continuing from above, what would Python print?

print('colin kaepernick' in superbowls)
#Prints: False

print(len(superbowls))
#Prints: 4

print(superbowls['peyton manning'] == superbowls['joe montana'])
#Prints: False

superbowls[('eli manning', 'giants')] = 2
print(superbowls)
#Prints: {'joe flacco': 1, 'joe montana': 4, ('eli manning', 'giants'): 2, 'tom brady': 3, 'peyton manning': 1}

superbowls[3] = 'cat'
print(superbowls)
#Prints: {'joe flacco': 1, 3: 'cat', 'joe montana': 4, ('eli manning', 'giants'): 2, 'tom brady': 3, 'peyton manning': 1}

superbowls[('eli manning', 'giants')] =  superbowls['joe montana'] + superbowls['peyton manning']
print(superbowls)
#Prints: {'joe flacco': 1, 3: 'cat', 'joe montana': 4, ('eli manning', 'giants'): 5, 'tom brady': 3, 'peyton manning': 1}

superbowls[('steelers', '49ers')] = 11
print(superbowls)
#Prints: {'joe flacco': 1, 3: 'cat', 'joe montana': 4, ('eli manning', 'giants'): 5, 'tom brady': 3, 'peyton manning': 1, ('steelers', '49ers') = 11}

# I:  Given a dictionary replace all occurrences of x as the value with y.

d = {1: {2:3, 3:4}, 2:{4:4, 5:3}}
def replace_all(d, x, y):
    for key in d.keys(): 
        if type(d[key]) == dict: 
            replace_all(d[key], x, y) 
        else: d[key] = y if d[key] == x else d[key]

replace_all(d,3,1)
print(d)

# J:  Given a (non-nested) dictionary delete all occurences of a value. You cannot delete items in a dictionary as you are iterating through it (google :) ).

d = {1:2, 2:3, 3:2, 4:3}
def rm(d, x):
    keys_to_del = [key for key in d.keys() if d[key] == x] 
    for key in keys_to_del: 
        del d[key]

rm(d, 2)
print(d)
