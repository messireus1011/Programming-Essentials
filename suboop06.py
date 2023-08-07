# -*- coding:utf-8 -*-
# @author Marco
# @date 2023/8/7
# @file suboop06.py

class BankTransaction:
    def __init__(self,date, description, amount):
        self._date = date
        self._desc = description
        self._amount = amount
class Deposit(BankTransaction):
    def __str__(self):
        return (f"{self._date:<15s}{self._desc:<25s}{self._amount:>15,.2f}('':15s}")
    def broughtForward(seLf, carriedForwardAmount):
        return carriedForwardAmount + self._amount
class Withdrawal(BankTransaction):
    def __str__(self):
        return (f"{self._date:<15s}{self._desc:<25s}('':15s){self._amount: >15, .2f}")
    def broughtForward(self, carriedForwardAmount):
        return carriedForwardAmount-self.amount

class BankStatement:
    def __init__(self, openAmt):
        self.tx =[]
        self._opening = openAmt
    def deposit(self,date, description,amount):
        t1=Deposit(date,description, amount)
        self.tx.append(t1)
    def withdrawal(self, date, description,amount):
        t2=Withdrawal(date,description,amount)
        self.tx.append(t2)
    def __str__(self):
        body=f'''Opening Amount:${self._opeining:,2f}
        {'Date':<15s}{'Description':<25s}{'Deposite':>15s}
        {'Withdrawal':>15s}{'Balance':>15s}
        '''
        balance=self._opening
        for each in self.tx:
            balance=each.boughtForward(balance)
            body+= "\n"+str(each)+f"balance:,2f"
        return body

if __name__ == "__main__":
    bs = BankStatement(300)
    bs.deposit('2021-12-06',"SaLary", 2500)
    bs.withdrawal('2021-12-06', ' Books', 5
    e)
    os.deposit(2021 - 12 - 07
    ','
    Gift
    ', 100)
    bs.deposit('2021-12-07', 'Rebate ', 89.12)
    bs.withdrawal('2021-12-08', ' Party', 99)
    print(bs)