from rlcard.utils.utils import rank2int


class KuhnPokerJudger(object):
    ''' The Judger class for Kuhn Poker
    '''

    def __init__(self, np_random):
        ''' Initialize a judger class
        '''
        self.np_random = np_random

    @staticmethod
    def judge_game(players):
        ''' Judge the winner of the game.

        Args:
            players (list): The list of players who play the game

        Returns:
            (list): Each entry of the list corresponds to one entry of players
        '''
        # Judge who are the winners
        winners = [0, 0]
        # If one player folds, the other player is the winner
        for idx, player in enumerate(players):
            if player.status == 'folded':
                winners[(idx+1) % 2] = 1
                break

        if sum(winners) < 1:
            p0_rank = rank2int(players[0].hand.rank)
            p1_rank = rank2int(players[1].hand.rank)
            winners = [1, 0] if p0_rank > p1_rank else [0, 1]

        # Compute the total chips
        total = 0
        for p in players:
            total += p.in_chips

        each_win = float(total) / sum(winners)

        payoffs = []
        for i, _ in enumerate(players):
            if winners[i] == 1:
                payoffs.append(each_win - players[i].in_chips)
            else:
                payoffs.append(float(-players[i].in_chips))

        return payoffs
