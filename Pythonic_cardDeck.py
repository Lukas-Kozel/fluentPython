import collections
import random

Card = collections.namedtuple('Card',['rank','suit'])

class Deck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
    
suit_values = dict(spades =3, hearts =2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = Deck.ranks.index(card.rank)
    return rank_value*len(suit_values)+suit_values[card.suit]

def set_card(deck, position, card):
    deck._cards[position] = card
        
        
# newDeck = Deck()
# print("lol")
# randomCard = newDeck.__getitem__(random.randint(0,newDeck.__len__()))
# print(randomCard)
# print(newDeck[-1])
# print(newDeck[:3])
# print (randomCard in newDeck)

# for card in sorted(newDeck,key=spades_high):
#     print(card)