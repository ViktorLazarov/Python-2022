from random import shuffle


# Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades")
# Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
# Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
# Card 's __repr__  method should return the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


card1 = Card("A", "Spades")


# 1.Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .
# 2.Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
# 3.Deck 's __repr__  method should return information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
# 4.Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the end of the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt".
# 5.Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from the deck, this method should raise a ValueError  with the message "Only full decks can be shuffled". shuffle should return the shuffled deck.
# 6.Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck and return that single card.
# 7.Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list of cards from the deck and return that list of cards.

class Deck:
    def __init__(self):
        suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        # List Comprehension
        self.cards = [Card(value, suit) for value in values for suit in suits]

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

        # for suit in suits:
        #     for value in values:
        #         self.cards.append(Card(value, suit))
        # print(self.cards)

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        cards_in_deck = self.count()
        removed_cards = min([num, self.count()])
        if removed_cards == 1:
            print("Going to remove {} card".format(removed_cards))
        else:
            print("Going to remove {} cards".format(removed_cards))
        if cards_in_deck == 0:
            raise ValueError("All cards have been dealt")
        dealt_cards = self.cards[-removed_cards:]
        self.cards = self.cards[:-removed_cards]
        return dealt_cards

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)


d = Deck()
d.shuffle()
print(d.count())
print(d.cards)
d.shuffle()
print(d.deal_hand(5))
