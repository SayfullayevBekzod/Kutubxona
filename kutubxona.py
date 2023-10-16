from qavat import Qavat
from kitob import Kitob
from shkaf import Shkaf

class Kutubxona:
    
    def __init__(self) -> None:
        self.qavat_list: list[Qavat] = [Qavat(i) for i in range(1, 4)]

    def contain(self, kitob: Kitob):
        for qavat in self.qavat_list:
            if qavat.contain(kitob) is not None:
                return qavat.contain(kitob)
        return None

    def add(self, kitob: Kitob, qavat: int, shkaf: str, javon: int):
        return self.qavat_list[qavat - 1].add(kitob, shkaf, javon)

    def get_books(self, qavat, shkaf):
        qavat_in = self.qavat_list[qavat - 1]
        for shkaf_in in qavat_in.shkaf_list:
            if shkaf_in.idn == shkaf:
                print(f"shkaf --> {shkaf_in.idn}")
                shkaf_in.display_all_books()
    
    def get_position(self, kitob:Kitob):
        for qavat in self.qavat_list:
            if qavat.get_position(kitob) != None:
                return " qavat --> " + str(qavat.number_qavat) + qavat.get_position(kitob)

    def find(self, muallifi, nomi):
        kitob = Kitob(nomi, muallifi)
        return "shu yerga boring sizni kitob kutayapti:)" + self.get_position(kitob)

        