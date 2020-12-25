# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 23:14:26 2020

@author: okkes
"""

FirstName=input("Please enter your name: ")
LastName=input("Please enter your lastname: ")
Age=input("Please enter your age: ")
DateOfBirth=input("Please enter your date of birth(just year): ")

userIdenty=[FirstName,LastName,Age,DateOfBirth]

for i in userIdenty:
	print(i)
	
	
if (int(Age)<18 or int(DateOfBirth)>2002):
    print("You can not go out because it is too dangerous")
else:
    print("You can go out to the street.")