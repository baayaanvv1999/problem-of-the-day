# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fTI-0hmufaiaKBrH4dxSSozu8q1XC1hD
"""

s = input("Enter a string: ")
n = len(s)

if n < 2:
   result = s
else:
   start, max_len = 0, 1

   for i in range(n):
       # check odd-length palindromes
       left, right = i - 1, i + 1
       while left >= 0 and right < n and s[left] == s[right]:
           if right - left + 1 > max_len:
               start = left
               max_len = right - left + 1
           left -= 1
           right += 1

       # check even-length palindromes
       left, right = i, i + 1
       while left >= 0 and right < n and s[left] == s[right]:
           if right - left + 1 > max_len:
               start = left
               max_len = right - left + 1
           left -= 1
           right += 1

   result = s[start:start + max_len]

print("Longest palindromic substring:", result)

s = input("Enter a string: ")
n = len(s)

if n < 2:
   result = s
else:
   start, max_len = 0, 1

   for i in range(n):
       # check odd-length palindromes
       left, right = i - 1, i + 1
       while left >= 0 and right < n and s[left] == s[right]:
           if right - left + 1 > max_len:
               start = left
               max_len = right - left + 1
           left -= 1
           right += 1

       # check even-length palindromes
       left, right = i, i + 1
       while left >= 0 and right < n and s[left] == s[right]:
           if right - left + 1 > max_len:
               start = left
               max_len = right - left + 1
           left -= 1
           right += 1

   result = s[start:start + max_len]

print("Longest palindromic substring:", result)