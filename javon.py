from kitob import Kitob

class Javon:
    
    def __init__(self, number: int) -> None:
        self._number = number
        self.kitob_list: list[Kitob] = []

    @property
    def number(self):
        return self._number
        
    def contain(self, kitob: Kitob):
        for kitob_ in self.kitob_list:
            if kitob_.muallifi == kitob.muallifi and kitob_.nomi == kitob.nomi:
                return kitob
        return None

    def add(self, kitob: Kitob):
        if len(self.kitob_list) < 10:
            self.kitob_list.append(kitob)
            return "Ok"
        else:
            return None

    