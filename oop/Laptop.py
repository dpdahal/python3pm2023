class Laptop:
    price =20000
    def brand(self,name):
        print("Brand Name: ",name)

class Dell(Laptop):
    # price = 30000
    def quantity(self,quantity):
        print("Quantity: ",quantity * self.price)

obj = Dell()
obj.brand('Dell')
obj.quantity(2)


