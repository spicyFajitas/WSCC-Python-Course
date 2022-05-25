#defines first funtion
def calculateOvertime(hours, rate):
	#calculates total overtime
	
	#defines circumstance and then calculates based on circumstances
    if hours<=40:
        #calculates normal pay
        pay=hours*rate
    else:
        #calculates overtime hours
        overtime=hours-40
        #calculates overtime pay
        pay=40*rate+(1.5*rate)*overtime
	#prints specification totals
    print("Your total pay is>>    $", pay)

#defines main function
def main():
	#collects inputs
    hours=eval(input("Enter hours worked>> "))
    rate=eval(input("Enter hourly wage>>  "))
    print()
    print()
    #calls function
    calculateOvertime(hours, rate)
    main()


main()