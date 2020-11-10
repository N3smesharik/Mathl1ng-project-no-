class Ticket:
    def __init__(self, wfrom, to, price, seatClass):
        self.wfrom = wfrom
        self.to = to
        self.price = price
        self.seatClass = seatClass
    def info(self):
        print(self.wfrom, self.to, self.price, self.seatClass)
class Passenger:
    money = 0
    def __init__(self, money):
        self.money = money
    def buy(self, wfrom, to, price, seatClass):
        ticket = Ticket(wfrom, to, price, seatClass)
        if ticket.price > self.money:
            print("You need more money. Now you have", self.money)
        else:
            self.money -= ticket.price
            print("Your ticket:", ticket.wfrom, ticket.to, ticket.price, ticket.seatClass)
            print("Succesfully! You have", self.money)
I = Passenger(125)
CORESH = Passenger(50)
I.buy("A", "B", 125, 1)
CORESH.buy("A", "B", 125, 1)
