from javon import Javon
from kitob import Kitob

class Shkaf:

    def __init__(self, idn) -> None:
        self._idn = idn
        self.javon_list: list[Javon] = [Javon(i) for i in range(1, 7)]

    @property
    def idn(self):
        return self._idn

    def contain(self, kitob: Kitob):
        for javon in self.javon_list:
            if javon.contain(kitob) != None:
                return javon.contain(kitob)
        return None
    
    def add(self, kitob: Kitob, number_javon: int):
        javon: Javon = self.javon_list[number_javon - 1]
        return javon.add(kitob)

    def display_all_books(self):
        for javon in self.javon_list:
            for kitob in javon.kitob_list:
                print(f"{kitob.muallifi}, {kitob.nomi}")
    
    def get_position(self, kitob:Kitob):
        for javon in self.javon_list:
            if javon.contain(kitob) != None:
                return " javon --> " + str(javon.number)
        return None