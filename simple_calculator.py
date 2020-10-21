
print("This is simple calculation program")


UserName = input("\nPlease, enter your name: ")


A = input("Enter variable A: ")
B = input("Enter variable B: ")
C = input("Enter variable C: ")

MathCalc = ((int(A) + int(B)) * int(C))

print("\nHello " + UserName.capitalize() + "!")

print("\nCalcultion results for","(",str(A),"+",str(B),")","*",str(C),"is",str(MathCalc))