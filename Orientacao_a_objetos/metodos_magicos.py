"""
https://rszalski.github.io/magicmethods/
"""

class A:
    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(cls, '_jaexiste'):
    #         cls._jaexiste = object.__new__(cls)

    #     return cls._jaexiste
    
    def __init__(self):
        print('Eu sou o __init__')
    
    def __call__(self, *args, **kwds):
        resultado = 1

        for i in args:
            resultado *= i
        
        return resultado

a = A()
b = A()
c = A()

print(a == b and b == c)
print(id(a), id(b), id(c))

d = A()
var = d(1,2,5,6,8,11,9)
print(var)
