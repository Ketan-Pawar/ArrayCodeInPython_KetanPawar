# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 20:23:03 2022

@author: Sanjay
"""

import numpy as npy


# Using for loop
# a = []
# count = int(input("Enter the size of an array: "))

# for i in range(0,count):
#     l = int(input())
#     a.append(l)
# print(a)

# By using slicing
# a = int(input("Number of elements in an array: "))
# num = list(map(int, input("Enter an elements: ").strip().split()))
# print("Entered array is : ",num)
# print("Reversed array is : ",num[::-1])

# By using reverse function
a = int(input("Number of elements in an array: "))
num = list(map(int, input("Enter an elements: ").strip().split()))
print("Entered array is : ",num)
num.reverse()
print("Reversed array using Reverse Function: ",num)


# The flip() method in the NumPy module reverses the order of
# a NumPy array and returns the NumPy array object.
#The original NumPy array
# new_arr=npy.array(['S','E','A','R','C','I','A','N','S'])
# print("Original Array is :",new_arr)
 
# #reversing using flip() Method
# res_arr=npy.flip(new_arr)
# print("Resultant Reversed Array:",res_arr)

