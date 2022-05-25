from Card import *

def main():

    numberCards=inputs()
    cards=Card(numberCards)
    hand=cards.createCardDeck()
    cardsLeft=cards.cardsLeft()
    print("\nYour hand is:", hand, "\n\nYou have", cardsLeft, "cards left.")

def inputs():
  n = 0
  while n < 1: #very nifty error handling that Levi showed me
    try:
      n = eval(input("\nHow many cards do you want? "))
      if n < 1 or type(n) == float or n > 52:
        print("\nInvalid number"); n = 0
    except:
      print("\nInvalid input")
  return n
main()

'''
def inputs():
  try:     #error handling that I tried to create similar            #to Levi's that would be implimented differently
    n=0
    n=eval(input("Enter number of cards desired for your hand>> "))
    if n<1 or n>52 or type(n)==float:
      print("Please check your input and try again.")
      n=0
      inputs()
    else:
      return n
      
  except:
    main()
  return n
main()
'''