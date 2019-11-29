# AttributeError Example
try:
    a=input()
    a.reverse()
except AttributeError:
    print("AttributeError Found")

# TypeError Example
try:
    a=input()
    b=2
    c=a+b
except TypeError:
    print("TypeError Found")

# ValueError Example
try:
    a=int('aa')
except ValueError:
    print("ValueError")
