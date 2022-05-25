#create function to calculate windchill values
def calcWindchill(T,W):
	return 35.74 + 0.6215*T-35.75*(W**0.16) + 0.4275*T*(W**0.16)
	
#create function to setup table
def setupTable():
	#intro
	print("This program prints a table of wind chill values from specified intervals.")
	#x-axis lable
	print("Temperature (degrees F)->")
	#y-axis label
	print("Wind Speed -mph (below)", end = "")
	#prints temperature values from -20 to 60 at intervals of 10
	for T in range(-20, 61, 10):
		print(format(T, "8d"), end = "")
	print("\n","-"*94)
	#formatting
	for T in range(-20, 61, 10):
		print("      ", end = "")
	print("       ")

#defines main
def main():
	#calls table setup function
	setupTable()
	#for each wind speed value, print wind speed and run loop for windchill values
	  #this loops just has an extra space in the "print(W," ... ",end = "    ")" string 
	  #to make the table values line up better
	for W in range(0, 10, 5):
		print(W, "                     ", end = "    ")
		#for each temperature value, run calculation and print value
		for T in range(-20, 61, 10):
			calcWindchill(T,W)
			print(format(calcWindchill(T,W), '6.2f'), end = '  ')
		print()
	#runs the same loop
	for W in range(10, 53, 5):
		print(W, "                    ", end = "    ")
		#for each temperature value, run calculation and print value
		for T in range(-20, 61, 10):
			calcWindchill(T,W)
			print(format(calcWindchill(T,W), '6.2f',), end = '  ')
		print()
main()