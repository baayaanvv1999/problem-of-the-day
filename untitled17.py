# -*- coding: utf-8 -*-
"""Untitled17.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jpwwktj_z2na_JIQXjyTzVBJxVSTLkzl
"""

n = int(input("Enter the number of elements in the array: "))
Arr = []
for i in range(n):
   num = int(input("Enter element " + str(i+1) + ": "))
   Arr.append(num)

leaders = []
max_right = arr[-1]
leaders.append(max_right)

for i in range(len(arr)-2, -1, -1):
   if arr[i] > max_right:
       max_right = arr[i]
       leaders.append(max_right)
print("Leaders in the array:", leaders)