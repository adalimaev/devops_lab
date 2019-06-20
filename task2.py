#!/usr/bin/env python

s = input("Enter your string: ")

if s == s[::-1]:
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")
