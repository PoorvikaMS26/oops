class Payment:
    def pay(self):
        print("processing Payment:")
class GooglePay(Payment):
    def pay(self):
        print("payment through Googlepay:")
class Phonepe(Payment):
    def pay(self):
        print("Payment through Phonepe")
class CreditCard(Payment):
    def pay(self):
        print("Payment through CreditCard:")
P=Payment()
G=GooglePay()
Ph=Phonepe()
C=CreditCard()
P.pay()
G.pay()
C.pay()
    