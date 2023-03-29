import random
class Card:
    """Represents a standard playing card."""
    
    suit_names = ['Clubs', 'Diamons', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    
    def __init__(self, suit = 0, rank =2):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])
    
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self, card):
        self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def sort(self):
        self.cards.sort()
    
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
    
    def deal_hands(self, players, players_cards):
        hands = list()
        for x in range(players):
            hands.append(Hand('Player {}'.format(x+1)))
            for i in range(players_cards):
                hands[x].add_card(self.pop_card())
        return hands

class Hand(Deck):
    """Represents a hand of playing cards."""

    def __init__(self, label = ''):
        self.cards = []
        self.label = label

def find_defining_class(obj, meth_name):
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty



  
if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    #print(deck)
    hands = deck.deal_hands(4, 2)
    for x in range(len(hands)):
        print('Player {}:\n{} \n'.format(x+1, hands[x]))