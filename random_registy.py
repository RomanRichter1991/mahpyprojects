#!/usr/bin/env python3

##############################################################################
# Program prints entered name in random registry
##############################################################################

# import module "random"
import random

# name input
name = input("Enter your name: ")

# randomly select registry
rnname = [name.capitalize(), name.upper(),
          name.swapcase(), name.lower()]

# print out result
print(
    random.choice(rnname)
)
