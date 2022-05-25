import math
def area():
	a,b,c=eval(input("Enter the lengths of the three sides of the triangle separated by commas for a, b, c:  "))

	perim=(a+b+c)
	mP=perim/2
	area=math.sqrt(mP*(mP-a)*(mP-b)*(mP-c))
	print()
	print("The area of the triangle is", round(area,3), "square units.")
	#a	+	b	+	c 
	#2
	return

def main():
	area()
main()