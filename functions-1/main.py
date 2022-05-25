
#Declare functions 


def happy():
  print("Happy birthday to you!")

def SingLucy():
  happy()
  happy()
  print("Happy birthday, dear Lucy!")
  happy()
  print("")

#pass a string argument/parameter
def Sing(person):
  happy()
  happy()
  #use that string argument
  print("Happy birthday, dear", person + "!")
  happy()
  print("")

  

def main():
  #call happy function
  happy()
  happy()
  print("Happy birthday, dear Fred!")
  happy()
  print("")

  input("Press enter to continue...\n")
  #call SingLucy Function
  SingLucy()

  input("Press enter to continue...\n")
  #pass a string to the sing function
  Sing("John")

  input("Press enter to continue...\n")

  # decalare a variable and then pass a string to the Sing function
  sally = "Sally"
  Sing(sally)

  input("Press enter to continue...\n")
  # decalare a variable and then pass a string based on user input to the Sing function 
  name = input("Enter a name\n")

  Sing(name)

main()