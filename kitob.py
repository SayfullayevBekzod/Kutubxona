class Kitob:

    _nomi: str
    _muallifi: str

    def __init__(self, nomi = None, muallifi = None) -> None:
        self._nomi = nomi
        self._muallifi = muallifi

    @property
    def nomi(self):
        return self._nomi

    @property
    def muallifi(self):
        return self._muallifi

    def __str__(self):
        return self._muallifi + ", " + self._nomi