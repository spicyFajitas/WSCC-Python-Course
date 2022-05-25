#defines function
def BMI(w,h):
		#calculates BMI
		i=(w*720)/(h*h)
		print()
		#calculates output
		print(round(i,4))
		#returns different message based on output calculated
		if 19<=i<=25:
			print("\nYour body mass index is healthy.")
		if i<19:
			print("\nYour body mass index is below the healthy range. You might consider eating more and building muscle mass.")
		if i>25:
			print("\nYour body mass index is above the healthy range. You might consider eating healthier and working out on a more regular basis.")

#defines main
def main():
	#tries this first
	try:
		w, h = eval(input("Enter in your weight in pounds and height in inches, respectively, separated by a comma>> "))
		BMI(w,h)
	#if the first try doesn't work then we throw up one of these errors

	except ZeroDivisionError:
		print("\nYou're not 0 inches tall.\nDon't be that guy.")
		print(ZeroDivisionError)
main()