
UserName = input("Please, enter your name: ")


A = input("Enter variable A: ")
B = input("Enter variable B: ")
C = input("Enter variable C: ")

MathCalc = ((int(A) + int(B)) * int(C))

input("\nHello " + UserName.upper() + "!" + "\nPress Enter to see calculation results!")

print("\nCalcultion Result for:",str(A),"+",str(B),"*",str(C),"=",str(MathCalc))