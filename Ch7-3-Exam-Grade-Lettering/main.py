#defines function
def program(x):
	#says what to do based on different parameters
	if 90<=x<=100:
		print("\nA\n\nCongrats! You did good!")
	elif 80<=x<90:
		print("\nB\n\nGood work!")
	elif 70<=x<80:
		print("\nC\n\nNot bad, good effort.")
	elif 60<=x<70:
		print("\nD\n\nYou need to pick up the slack before you fall too far behind.")
	elif x<60:
		print("\nF")
		print("\nSTOP BEING LAZY!")
	elif 100<x<=110:
		print("\nA+\n\nEXTRA CREDIT!! WOOT WOOT!!!")
	elif 110<x<=120:
		print("That's insane. Just. Insane.")
	elif 120<x:
		print("\nAre you telling the truth?")

#defines main
def main():
	#input
	x=eval(input("What was your exam grade?>> "))
	#calls function
	program(x)
main()