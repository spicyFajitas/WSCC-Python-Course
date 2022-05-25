

def TextToNum():
  print("This program converts a textual message into a sequence")
  print("of numbers representing the Unicode encoding of a message")

  #get the message to encode
  message = input("Please enter the message to encode:")

  print("\nHere are the Unicode codes:")

  #Loop through the message and print out the Unicode values
  #https://docs.python.org/3.5/library/functions.html#ord
  for ch in message:
    print(ord(ch), end = " ")

  #blank line
  print("")

def NumToText():
  #This method converts a sequence of Unicode Numbers into a string of text
  print("This program converts a sequence of Unicode Numbers into ")
  print("the string of text it represents. \n")

  #enter encoded message
  inString = input("Please enter the Unicode-encoded message: ")

  #loop through each substring and build Unicode message
  message = ""

  for numStr in inString.split():
    codeNum = eval(numStr)           #convert digits to a number
    message = message + chr(codeNum) #concatenate character to message

  print("\nThe decoded message is:", message)
  
def NumToTextEff():
  #This method converts a sequence of Unicode Numbers into a string of text
  print("This program converts a sequence of Unicode Numbers into ")
  print("the string of text it represents. \n")

  #enter encoded message
  inString = input("Please enter the Unicode-encoded message: ")

  #loop through each substring and build Unicode message
  chars = []

  for numStr in inString.split():
    codeNum = eval(numStr)           #convert digits to a number
    chars.append(chr(codeNum))       #concatenate character to message

  message = "".join(chars)
  print("\nThe decoded message is:", message)


def caesar(plainText, shift): 
  cipherText = ""
  for ch in plainText:
    if ch.isalpha():
      stayInAlphabet = ord(ch) + shift 
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter
  print ("Your ciphertext is: ", cipherText)
  
