class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to ",self.name,self.lastName,"'s cart")

customer1 = Customer()
customer1.name = "Siwakorn"
customer1.lastName = "C"
customer1.addCart()

customer2 = Customer()
customer2.name = "Kittinan"
customer2.lastName = "I"
customer2.addCart()

customer3 = Customer()
customer3.name = "Wasin"
customer3.lastName = "O"
customer3.addCart()

customer4 = Customer()
customer4.name = "Pongsakorn"
customer4.lastName = "K"
customer4.addCart()