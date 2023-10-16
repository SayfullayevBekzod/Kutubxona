from shkaf import Shkaf
from kitob import Kitob

class Qavat:

    def __init__(self, number_qavat: int) -> None:
        self._number_qavat = number_qavat
        self.shkaf_list: list[Shkaf] = [Shkaf(f"C {i}") for i in range(1, 31)]

    @property
    def number_qavat(self):
        return self._number_qavat

    def contain(self, kitob: Kitob):
        for shkaf in self.shkaf_list:
            if shkaf.contain(kitob) is not None:
                return shkaf.contain(kitob) 
        return None
            
    def add(self, kitob: Kitob, shkaf: str, javon: int):
        for shkaf_ in self.shkaf_list:
            if shkaf_.idn == shkaf:
                return shkaf_.add(kitob, javon)
        return None
    
    def get_position(self, kitob:Kitob):
        for shkaf in self.shkaf_list:
            if shkaf.get_position(kitob) != None:
                return " shkaf --> " + str(shkaf.idn) + shkaf.get_position(kitob)
        return None
    
