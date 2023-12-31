# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xz6h4kcV6hbugaAjMo_WbmFJJVM0DTAc
"""

import math

def calculate_cone_size(radius, height):
   # Calculate the volume of the cone
   volume = (1/3) * math.pi * (radius**2) * height

   # Calculate the surface area of the cone
   slant_height = math.sqrt(radius**2 + height**2)
   surface_area = math.pi * radius * (radius + slant_height)

   return volume, surface_area

radius = float(input("Enter the radius of the cone: "))
height = float(input("Enter the height of the cone: "))

cone_volume, cone_surface_area = calculate_cone_size(radius, height)
print("The volume of the cone is:", cone_volume)
print("The surface area of the cone is:", cone_surface_area)