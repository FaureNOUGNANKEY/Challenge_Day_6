# Microsoft Windows [version 10.0.26100.4652]
# (c) Microsoft Corporation. Tous droits réservés.

# C:\Users\HP>python
# Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> print 'hello world'
#   File "<python-input-0>", line 1
#     print 'hello world'
#     ^^^^^^^^^^^^^^^^^^^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
# >>> print ('hello world')
# hello world
# >>> print (age)
# Traceback (most recent call last):
#   File "<python-input-2>", line 1, in <module>
#     print (age)
#            ^^^
# NameError: name 'age' is not defined
# >>> age = 25
# >>> print (age)
# 25
# >>> numbers = [1, 2, 3, 4, 5]
# >>> numbers[5]
# Traceback (most recent call last):
#   File "<python-input-6>", line 1, in <module>
#     numbers[5]
#     ~~~~~~~^^^
# IndexError: list index out of range
# >>> import maths
# Traceback (most recent call last):
#   File "<python-input-7>", line 1, in <module>
#     import maths
# ModuleNotFoundError: No module named 'maths'
# >>> import math
# >>> math.PI
# Traceback (most recent call last):
#   File "<python-input-9>", line 1, in <module>
#     math.PI
# AttributeError: module 'math' has no attribute 'PI'
# >>> math.pi
# 3.141592653589793
# >>> users = {'name':'Asab', 'age':250, 'country':'Finland'}
# >>> users['name']
# 'Asab'
# >>> users['county']
# Traceback (most recent call last):
#   File "<python-input-13>", line 1, in <module>
#     users['county']
#     ~~~~~^^^^^^^^^^
# KeyError: 'county'
# >>> users['country']
# 'Finland'
# >>> 4+'3'
# Traceback (most recent call last):
#   File "<python-input-15>", line 1, in <module>
#     4+'3'
#     ~^~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# >>> 4 + int ('3')
# 7
# >>> 4 + float ('3')
# 7.0
# >>> from math import power
# Traceback (most recent call last):
#   File "<python-input-18>", line 1, in <module>
#     from math import power
# ImportError: cannot import name 'power' from 'math' (unknown location)
# >>> from math import pow
# >>> pow(2,3)
# 8.0
# >>> int ('12a')
# Traceback (most recent call last):
#   File "<python-input-21>", line 1, in <module>
#     int ('12a')
#     ~~~~^^^^^^^
# ValueError: invalid literal for int() with base 10: '12a'
# >>> 1/0
# Traceback (most recent call last):
#   File "<python-input-22>", line 1, in <module>
#     1/0
#     ~^~
# ZeroDivisionError: division by zero
# >>>