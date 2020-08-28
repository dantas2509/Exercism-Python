import _thread
STATUS_NEW = 'new'
STATUS_OPEN = 'opened'
STATUS_CLOSED = 'closed'


class BankAccount:
    def __init__(self):
        self.status = STATUS_NEW
        self.balance = 0
        self.mutex = _thread.allocate_lock()

    def get_balance(self):
        self.checkStatus()
        return self.balance

    def open(self):
        self.checkStatus(oper='open')
        self.status = STATUS_OPEN

    def deposit(self, amount):
        self.mutex.acquire()
        self.checkStatus()
        if amount < 0:
            raise ValueError('It is impossible to deposit negative values')
        else:
            self.balance += amount
        self.mutex.release()

    def withdraw(self, amount):
        self.mutex.acquire()
        self.checkStatus()
        if amount < 0:
            raise ValueError('It is impossible to withdraw negative values')
        elif amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError('This account does not have enough money.')
        self.mutex.release()

    def close(self):
        self.checkStatus()
        self.withdraw(self.balance)
        self.status = STATUS_CLOSED

    def checkStatus(self, oper='normal'):
        if self.status != STATUS_OPEN and oper == 'normal':
            raise ValueError(f'This account is {self.status}. This operation is not possible')
        elif self.status == STATUS_OPEN and oper == 'open':
            raise ValueError(f'This account is already {self.status}. This operation is not possible')
