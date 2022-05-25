from Sphere import *
def main():
    #try catch
	try:
        #input
		radius=(eval(input("Enter the radius of a sphere>>")))
        #create object
		s=Sphere(radius)

        #outputs
		print("\nThe radius of the sphere is {}.".format(s.getRadius()))
		print("\nThe surface area of the sphere is {}.".format(round(s.surfaceArea(),3)))
		print("\nThe volume of the sphere is {}.".format(round(s.volume(),3)))
    #try catch
	except:
		print("\nThere was an error processing your request.\nError code 43152.")
main()