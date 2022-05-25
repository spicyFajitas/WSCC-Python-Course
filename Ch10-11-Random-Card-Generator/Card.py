import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def getRank(self):
        numberDictionary =  {1:"Ace", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Jack", 12:"Queen", 13:"King"}
        cardRank = numberDictionary[self.rank]
        return cardRank
     
    def getSuit(self):
       
        suit = ["Spades","Diamonds", "Clubs", "Hearts"]
        return random.choice(suit)
   
    def blackJackValue(self):
        if self.rank < 10:
          return self.rank

        else:
          rank = 10
          return rank
   
    def __str__(self, rank, suit):
        cardString = rank, 'of', suit
        cardString = " ".join(cardString)
        return cardString