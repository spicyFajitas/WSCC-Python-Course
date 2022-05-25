from Cards import *



def main():
  Player1=[]
  Player2=[]
  cards=Cards()
  #create deck of cards
  deck=cards.createCardDeck()
  
  #deal deck (using modulo)
  for i in range(len(deck.cards)):
    if i % 2 == 0:
      Player1.append(deck.cards[i])
    else:
      player2.append(deck.cards[i])
  
  for x in range Player1:
    print(x)
  for y in range Player2:
  
  #.pop cards to compare rank
  
  #append both cards to winner
  
  #what about if there's a war?
main()

def War():
  def __init__(self, Player1, Player2):
    self.Player1=Player1
    self.Player2=Player2
  
def getRank(self, rank):
    rank=rank.split(" ",1)
    cardRank = self.rankDictionary[int(rank[0])]
    return cardRank

def getSuit(self, suit):
    suit=suit.split(" ",1)
    cardSuit = self.suitDictionary[suit[1]]
    return cardSuit