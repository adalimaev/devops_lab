#!/usr/bin/env python

s = input().split()
temp = []

for i in s:
    temp.append(i[::-1])

out = " ".join(temp)
print(out)
