class Product ():
    def __init__(self,name,price,quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
    def Nread(self):
        return self.__name
    def Pread(self):
        return self.__price
    def Qread(self):
        return self.__quantity
    def getcost(self):
        return self.__price * self.__quantity
    