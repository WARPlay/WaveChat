import math


a = int(input())
b = int(input())
c = int(input())
x1 = 0
x2 = 0
s = 0
discr = b ** 2 - 4 * a * c
if discr < 0:
    print("NS")
else:
    if discr == 0:
        x1 = -b / (2 * a)
        x2 = x1
    else:
        x1 = (-b + discr ** 0.5) / (2 * a)
        x2 = (-b - discr ** 0.5) / (2 * a)
s = x1 * x2 * (315/5 - 13)
print(round(s, 4))