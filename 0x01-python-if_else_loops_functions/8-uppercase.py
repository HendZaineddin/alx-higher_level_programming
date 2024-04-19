#!/usr/bin/python3
i = 0
while(str(i) != '\0'):
    if (ord(str(i)) >= 97) and (ord(str(i)) <= 122):
        print(str(i) + "A")
    else:
        continue
