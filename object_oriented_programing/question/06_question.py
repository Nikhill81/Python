# Can you change the self-parameter inside a class to something else(say). try change self "slf" or "harry" and see the effects

from random import randint
class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book (self, fro, to):
        print(f"Ticket is booked in train no: :{self.trainNo} from {fro} to {to}")

    def getStatus (self, trainNo):
        print(f"Ticket no {self.trainNo} is running on time")

    def getFare(self, trainNo, fro, to ):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

t = Train(12399)
t.book("rampur", "delhi")

