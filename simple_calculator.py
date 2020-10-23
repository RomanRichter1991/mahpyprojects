#!/usr/bin/env python

# #####################################################################
# Simple calculation program
# ####################################################################

# print program title
print("This is simple calculation program")

# name input
Name = input("\nPlease, enter your name: ")

A = input("Enter variable A: ")
B = input("Enter variable B: ")
C = input("Enter variable C: ")

MathCalc = ((int(A) + int(B)) * int(C))

print("\nHello " + Name.capitalize() + "!")

print("\nCalculation results for ","(",str(A),"+",str(B),")","*",str(C),"is",str(MathCalc))

print("\nProgram finished...")
