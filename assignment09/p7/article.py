# article.py
# student.py
# CTMS-14
# a9 p7.py
# Ahmed Abasimel
# aabasimel@constructor.university
class Article:
    def __init__(self, name, category, brand, stock, price):
        """Constructor initializing all properties."""
        self._name = name
        self._category = category
        self._brand = brand
        self._stock = stock
        self._price = float(price)

    # Setter methods
    def setName(self, name):
        self._name = name

    def setCategory(self, category):
        self._category = category

    def setBrand(self, brand):
        self._brand = brand

    def setStock(self, stock):
        self._stock = stock

    def setPrice(self, price):
        self._price = float(price)

    # Getter methods
    def getName(self):
        return self._name

    def getCategory(self):
        return self._category

    def getBrand(self):
        return self._brand

    def getStock(self):
        return self._stock

    def getPrice(self):
        return self._price

    # Method to print all properties
    def printInfo(self):
        print(f"Name: {self._name}")
        print(f"Category: {self._category}")
        print(f"Brand: {self._brand}")
        print(f"Stock: {self._stock}")
        print(f"Price: ${self._price:.2f}")
