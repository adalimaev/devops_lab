#!/usr/bin/env python

n = int(input("Please enter n: "))
width = n.bit_length()

for i in range(1, n+1):
    print(str(i).rjust(width), oct(i)[2:].rjust(width),
          hex(i)[2:].capitalize().rjust(width), bin(i)[2:].rjust(width))
