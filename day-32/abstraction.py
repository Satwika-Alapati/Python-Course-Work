from abc import ABC,abstractmethod

class Phonepay(ABC):

    def senderinfo(self):
        print("You can enter their mobile number or scanner")
    def amount(self):
        print("You can enter amount")
    def pin(self):
        print("you need to enter the pin")

    @abstractmethod
    def transaction(self):
        pass

class HDFC(Phonepay):
    def transaction(self):
        print("Payment using hdfc bank")

class SBI(Phonepay):
    def transaction(self):
        print("Payment using sbi bank")

class UNION(Phonepay):
    def transaction(self):
        print("Payment using union bank")

class AXIS(Phonepay):
    def transaction(self):
        print("Payment using axis bank")

class ICICI(Phonepay):
    def transaction(self):
        print("Payment using icici bank")

name1=HDFC()
name1.senderinfo()
name1.amount()
name1.pin()
name1.transaction()

name2=HDFC()
name2.senderinfo()
name2.amount()
name2.pin()
name2.transaction()

name3=HDFC()
name3.senderinfo()
name3.amount()
name3.pin()
name3.transaction()
