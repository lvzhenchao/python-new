
# 当所用数值超过计算机自身的计算能力时，Python 会自动转用高精度计算（大数计算）
n = 78
print(n)
print(type(n))

x = 88888888888888
print(x)
print(type(x))

y = -7777777777
print(y)
print(type(y))

f1 = 12.5
print(f1)
print(type(f1))

f2 = 0.123
print(f2)
print(type(f2))

f3 = 12e4
print(f3)
print(type(f3))

f4 = 0.1+0.2
print(f4)
f5 = 0.1+0.1-0.2
print(f5)

# 对于这种需要非常精确的结果
import decimal
f44 = decimal.Decimal("0.1")+decimal.Decimal("0.2")
print(f44)
f55 = decimal.Decimal("0.1")+decimal.Decimal("0.1")-decimal.Decimal("0.2")
print(f55)

# fractions更加精确模块
from fractions import Fraction
print(10/3)
print(Fraction(10,3))


















