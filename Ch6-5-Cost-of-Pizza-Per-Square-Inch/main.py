import math
import time
#create variables/first input
d=eval(input("Enter the size (in inches) of the pizza:"))
a=(math.pi*(d/2)**2)
#function for area
def area():
	#output
	print("The area  of the pizza is", round(a,3), "square inches.")
	print()
	return
#function for price
def price():
	#input
  price=eval(input("Enter the price of the pizza $"))
  #create variable
  total=0
  #calculates
  total=(price/(math.pi*(d/2)**2))
	#output
  print("Your pizza costs", round(total, 3) , "dollars per square inch.")
#main function
def main():
	#calls area function
	area()
	#wait two seconds
	time.sleep(1.5)
	#calls price function
	price()
	return
main()