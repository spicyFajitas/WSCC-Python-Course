from string import *

#prints intro
print("This program calculates the numerical value of a name based on the letters in the name.\n")

#input
n=(input("Please enter full name:"))

#creates variable
total=0
#turns all letters to lowercase
newvar=n.lower()

#blank line for visual effect
print()

#calculates numeric value
for ch in newvar:	
		total=(total+ord(ch)-96)
#prints numeric value
print("The numeric value of your name is", total + ".")