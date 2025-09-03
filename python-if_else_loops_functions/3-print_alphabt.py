#!/usr/bin/python3
result = ""
for i in range(97, 123):
    if i != 113 and i != 101:
        result += chr(i)
print(result, end="")
