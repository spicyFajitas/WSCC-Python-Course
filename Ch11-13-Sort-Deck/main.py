from Card import *
from random import *

def main():
    #input
    cardFile=input("Enter file to read from>>")
    
    cardDeck=Card(cardFile)

    deckOfCards=cardDeck.makeDeck()
    
    print(deckOfCards)
main()