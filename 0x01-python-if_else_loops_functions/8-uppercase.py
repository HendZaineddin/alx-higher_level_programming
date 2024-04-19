#!/usr/bin/python3
i = 0
while(str(i) != '\0'):
    if (ord(str(i)) >= 97) and (ord(str(i)) <= 122):
        str(i) = ord(str(i)) - 32)
    print("{}".format(str(i)), end="")
    i+=1
print('\n')

