__author__ = 'tkessler'

from scipy import stats

class carddeck():
    def __init__(self):
        self.deck = []
        self.suits = ['H','D','C','S']
        for i in range(1,14):
            for s in self.suits:
                self.deck.append((s,i))

    def deal(self,n=1):
        if n <= len(self.deck):
            hand = []
            for card in range(n):
                hand.append(self.deck.pop(stats.randint.rvs(0,len(self.deck))))
            return hand

class player():
    def __init__(self):
        self.hand = []

    @property
    def valuesum(self):
        value = 0
        for (s,v) in self.hand:
            value+=v
        return value

    def hit(self, n):
        if self.valuesum < n:
            return True
        else:
            return False
    def receive(self,cardlist):
        for card in cardlist:
            self.hand.append(card)

if __name__=="__main__":
    D = carddeck()
    player1 = player()
    player2 = player()

    player1.receive(D.deal(2))
    player2.receive(D.deal(2))

    while player1.hit(17):
        player1.receive(D.deal())

    while player2.hit(17):
        player2.receive(D.deal())

    print("Player 1: %d" % player1.valuesum)
    if player1.valuesum == 21: print("    BLACKJACK! Player wins!")
    elif player1.valuesum > 21: print("    Player 1 busts\n")
    print("Dealer: %d" % player2.valuesum)
    if player2.valuesum > 21: print("    Dealer busts\n")

