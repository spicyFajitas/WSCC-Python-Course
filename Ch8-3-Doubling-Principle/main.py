#How to write the fucntion without the need of while loops:

		#eval(input("Enter the initial principle>> "))
		#eval(input("Enter the rate>>              "))
		#t=((2*p)/r)


#investment function
def doubleInvestment(p,r):
	#calculation variable
	double=2*p
	#calculation variable
	interest=p*r
	#counter
	total=0
	#counter
	count=0
	print()
	#this is where the magic happens
	while p<=double:
		#calculate interest
		p=p+interest
		#counts how many times interest is compiled
		count=count+1
	#output
	print("It will take", count, "years to double the principle.")
	#fun message
	if count>5:
		print("\nHave fun waiting  :/")

#creates main
def main():
	#try catch
	try:
	#inputs
		p=eval(input("Enter the initial principle>> "))
		r=eval(input("Enter the rate>>             "))
		
		if p>0:
			doubleInvestment(p,r)
		elif p<0:
			print("All moneys is counted in positive terms, whether they are gains or losses.")
		elif p==0:
			print("If your principle is 0, go look under the couch cushions for some change.")
	except TypeError:
		print("\nYour input was not in the correct form.\nTry revising your input.")
		print(TypeError)
	except SyntaxError:
		print("\nYour input seems a little funky.\nTry revising your input.")
		print(SyntaxError)
	except NameError:
		print("\nYou can't use letters.")
		print(NameError)
main()