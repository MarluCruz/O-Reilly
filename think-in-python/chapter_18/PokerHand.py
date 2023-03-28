"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

from ex_0001 import Hand, Deck
import matplotlib


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.
        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
    
    def has_pair(self):
        x = 1
        j = x
        for card in self.cards:
            for j in range(j, len(self.cards)):
                otherCard = self.cards[j]
                if card.rank == otherCard.rank:
                    return True
            x += 1
            j = x
        return False
    
    def has_twopair(self):
        x = 1
        j = x
        count = 0
        for card in self.cards:
            for j in range(j, len(self.cards)):
                otherCard = self.cards[j]
                if card.rank == otherCard.rank:
                    count += 1
                    if count == 2:
                        return True
            x += 1
            j = x
        return False

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

    def  classify(self):
        pair = self.has_pair()
        twopair = self.has_twopair()
        flush = self.has_flush()
        if flush:
            self.label = 'flush'
            return
        elif twopair:
            self.label = 'two pair'
            return
        elif pair:
            self.label = 'pair'
            return
        else:
            self.label = 'Without clasification'

def count_frequency():
    thisdict = {'flush': 0, 'two pair': 0, 'pair': 0, 'Without clasification': 0}
    for z in range(2):
        deck = Deck()
        deck.shuffle()
        for i in range(7):
            hand = PokerHand()
            deck.move_cards(hand, 7)
            hand.sort()
            hand.classify()
            thisdict[hand.label] += 1
    for x, i in thisdict.items():
        print('{} : {}'.format(x, i))

if __name__ == '__main__':
    # make a deck
    
    count_frequency()


    