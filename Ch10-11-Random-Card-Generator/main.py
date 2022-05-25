from Card import *
from random import *

def main():
    try:
        #input for how many times to loop
        loopie=eval(input("Enter how many randomly generated cards you want>>"))
        for i in range(loopie):
            #randomly selects a number that picks which card and suit is chosen
            inputRank = randrange(1, 14)
            inputSuit = randrange(1, 5)
            #object to get values
            playingCard = Card(inputRank, inputSuit)
            cardRank = playingCard.getRank()
            cardSuit = playingCard.getSuit()
            cardJackVal = playingCard.blackJackValue()
            #does some really nice formatting for us
            cardName = playingCard.__str__(cardRank, cardSuit)
            #outputs
            print("\nCard", i+1, "name:", cardName,"\nBlackjack Value:", cardJackVal)
    #exception handling with our nifty try catch
    except:
        print("\nPlease check your input and try again.\n")
        main()
main()