class Computer:

    # Constructor
    def __init__(self):
        self.__maxprice = "800"

    # Method
    def sell(self):
        print("Selling price: " + self.__maxprice)

    # Method
    def setMaxPrice(self, price):
        self.__maxprice = price


# Object creation
obj = Computer()

#update the maxprice
obj.__maxprice = "1000"
obj.sell()  

#using the method MaxPrice to update the MaxPrice
obj.setMaxPrice("1000")
obj.sell() 
