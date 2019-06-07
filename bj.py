from random import shuffle



class Dealer:
    
    def __init__(self, deck):
        self.deck = deck

    def shuffledeck(self):
        shuffle(self.deck)

    def giveacard(self):
        return self.deck.pop()

class Player:
    
    def __init__(self,hand,money):
        self.hand = hand
        self.money = money
        self.ingame = True

    def hit(self,card):
        self.hand.append(card)

    def showhand(self):
        [print(card) for card in self.hand]

    def stand(self):
        self.ingame = False

    def bet(self,amount):
        if(amount <= self.money):
            self.money -= amount
            return True
        else:
            return False
    
    def retire(self,currentbet):
        return self.money + currentbet//2
        

class Game:

    def __init__(self):
        self.dealer = Dealer([2,3,4,5,6,7,8,9,10,10,10,10,11])
        self.currentbet = 0

    def initiate(self):
        initialhand = []
        self.dealer.shuffledeck()
        [initialhand.append(self.dealer.giveacard()) for n in range(2)]
        self.player = Player(initialhand, 200)

    def hit(self):
        self.player.hit(self.dealer.giveacard())

    def stand(self):
        self.player.stand()
        return self.validatewiner()
        
    def bet(self,amount):
        if(self.player.bet(amount)):
            self.currentbet += amount
            return True
        else:
            return False

    def validatewiner(self):   
        result = 0 
        for card in self.player.hand:
            result+=card
        print('\n{}\n'.format(result))
        if(result == 21):
            return 'winner'
        elif(result > 21):
            return 'loser'
        else:
            return 'tables'

    def ongoing(self):
        print("BJ")
        self.initiate()
        print("\nYour Hand \n{}\n".format(self.player.hand))
        while True:
            print("\nActions: bet, hit, stand, show, retire \n")
            action = input("What do you want to do: ")

            #if not action in actions:
             #   print("Not a valid option \n")
              #  continue

            if action == 'bet':
                try:
                    if(self.bet(int(input('How much: ')))):
                        print('\nYour current balance is: {}\n'.format(self.player.money))
                    else:
                        print('\nNot enough balance')
                except Exception as e:
                    print('*****[Debug-Amount] '+str(e))
                    print('\n Bad entry ')
            
            elif action == 'hit':
                self.hit()
            
            elif action == 'stand':
                if(self.stand()=='winner'):
                    print('Winner')
                else:
                    print('Loser')
                    
                break

            elif action == 'show':
                self.player.showhand()

            elif action == 'retire':
                print('Current balance: {}'.format(self.player.retire(self.currentbet)))
                break

            else:
                print('Bad option')
                continue


def main():
    game = Game()
    game.initiate()
    game.ongoing()

            
main()


