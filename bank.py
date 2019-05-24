class Account:
    def __init__(self,owner,balance):
        self.owner = owner,
        self.balance = balance

    def __str__(self):
        return('Owner: {} \n Balance: {}'.format(self.owner,self.balance))

    def deposit(self,depositq):
        self.balance += depositq
        print("Deposit accepted")

    
    def witdrawal(self,witdrawalq):
        if self.balance >= witdrawalq:
            self.balance - witdrawalq
            print("Withdrawal accepted")
        else:
            print("Not enough balance, balace: {}",format(self.balance))

    def main():
        acc1 = Account('George',52.2)
        print(acc1)
        acc1.owner
        acc1.balance
        acc1.deposit(50)
        acc1.witdrawal(75)
        acc1.witdrawal(500)
    
main()
