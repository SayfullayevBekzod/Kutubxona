from kitob import Kitob
from kutubxona import Kutubxona

library = Kutubxona()

kitob1 = Kitob("nom1", "muallif1")
kitob2 = Kitob("nom2", "muallif2")
kitob3 = Kitob("nom3", "muallif3")
kitob4 = Kitob("nom4", "muallif4")

print(library.add(kitob1, 1, "C 1", 1))
print(library.add(kitob2, 1, "C 1", 1))
print(library.add(kitob3, 1, "C 1", 1))
print(library.add(kitob4, 2, "C 23", 4))

print(library.get_position(kitob4))
print(library.find("muallif4","nom4"))

# library.get_books(1, "C 1")
# library.get_books(1, "C 30")

