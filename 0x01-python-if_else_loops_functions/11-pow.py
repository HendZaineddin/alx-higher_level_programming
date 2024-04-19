#!/usr/bin/python3
def pow(a, b):
k = 0
if b == 0:
    return (1)
elif b < 0:
    b = b + -1
    for i in range(b):
        k += a / a
elif b > 0:
    for i in range(b):
        k += a * a
if a < 0:
    return (-k)
return (k)
