import sys
from pkg1 import mod

print("无'__init__'：", dir(mod))
print(mod, mod.__package__)
print(mod.__name__)
print(sys.path)


from pkg2 import mod


print(" ------ 有'__init__' ------ ")
print(mod)
print(dir(mod))
print(mod.__doc__)
print(mod.__file__)
print(mod.__name__)
print(mod.__package__)
print(sys.path)

print(__name__)
print(__file__)
print(__package__)
print(__doc__)
print(__import__)