c = 42e3
print(c)
z = complex(1.25)
print(z)

import math

print(math.ceil(252.4))
print(math.floor(252.4))
print(abs(-45.300))
print(round(100.2563, 3))

from numbers import Number
from decimal import Decimal
from fractions import Fraction

print(isinstance(2.0, Number))
print(isinstance(Decimal('2.0'), Number))
print(isinstance(Fraction(2, 1), Number))
print(isinstance("2", Number))

x = -5j

print(type(x))

print(int(2.999))

print(0b101)
print(0o10)
print(0x1F)

print(1.1 + 2.2)
print(3.3)

str1 = 'welcome'
print(str1*2)

str1 = "my isname isisis jameis isis bond";
sub = "is"
print(str1.count(sub, 4))