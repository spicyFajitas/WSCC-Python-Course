import random
#class
class Card:
  
  def __init__(self,cardFile):
    self.cardFile=cardFile
    
    self.rankDictionary =  {1:"Ace", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Jack", 12:"Queen", 13:"King"}
    self.suitDictionary = {"s":"Spades","d":"Diamonds","c":"Clubs", "h":"Hearts"}
  
  def getRank(self, rank):
    rank=rank.split(" ",1)
    cardRank = self.rankDictionary[int(rank[0])]
    return cardRank
  
  def getSuit(self, suit):
    suit=suit.split(" ",1)
    cardSuit = self.suitDictionary[suit[1]]
    return cardSuit
  
  def sortCards(self):
    infile=open(self.cardFile, 'r')
    unsorted=infile.readlines()
    unsorted=map(str.rstrip, unsorted)
    
    unsorted=sorted(unsorted, key=lambda x: float (x.split()[0]))
    
    sortedCards=sorted(unsorted, key = lambda f: f.split()[1])
    return sortedCards

  def makeDeck(self):
    infile=self.sortCards()
    
    cards=[]
    for i in range(len(infile)):
      
      cardRank=self.getRank(infile[i])
      
      cardSuit=self.getSuit(infile[i])
      
      cardName= "\n", cardRank, "of", cardSuit
      
      cardName= " ".join(cardName)
      
      cards.append(cardName)
    
    cards=" ".join(cards)

    return cards