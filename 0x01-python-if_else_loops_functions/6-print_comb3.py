#!/usr/bin/python3
k=1
for i in range (10):
    while(k < 10):
        if (i < 8):
            print("{}{}, ".format(i, k), end="")
        else:
            print("{}{}".format(i, k), end="\n")
        k += 1
    k = i + 2
