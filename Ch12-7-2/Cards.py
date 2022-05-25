import random

class Cards:
  def __init__(self,cards):
    self.cards=cards
    self.suitDictionary = {0:"Spades",1:"Diamonds", 2:"Clubs", 3:"Hearts"}
    self.rankDictionary =  {0:"Ace", 1:"Two", 2:"Three", 3:"Four", 4:"Five", 5:"Six", 6:"Seven", 7:"Eight", 8:"Nine", 9:"Ten", 10:"Jack", 11:"Queen", 12:"King"}

  def createCardDeck(self,cardDeck):
    cardDeck=[]
    for i in range(4):
      suit=self.suitDictionary[i]
      for i in range(13):
        rank=self.rankDictionary[i]
        cardString = "\n",rank, 'of', suit
        cardString=" ".join(cardString)
        cardDeck.append(cardString)

    cardDeck=self.shuffleCardDeck(cardDeck)
    return cardDeck