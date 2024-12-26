
class cop:
    def __init__(self):
        self.__mp = 900
    def sell (self):
     print("selling price is",self.__mp)
    def setmp (self,price):
       self.__mp = price
c = cop()
c.sell()
c.__mp = 1000
c.sell()
c.setmp(100)
c.sell()    


