from rlcard.core import Card
from rlcard.games.limitholdem import Dealer


class KuhnPokerDealer(Dealer):

    def __init__(self, np_random):
        ''' Initialize a Kuhn Poker dealer class
        '''
        self.np_random = np_random
        self.deck = [Card('H', 'J'), Card('H', 'Q'), Card('H', 'K')]
        self.shuffle()
        self.pot = 0
