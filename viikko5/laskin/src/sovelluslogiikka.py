class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos

    def miinus(self, arvo):
        self.edellinen = self.tulos
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.edellinen = self.tulos
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.edellinen = self.tulos
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.edellinen = self.tulos
        self.tulos = arvo

class Summa:
    def __init__(self, sovellus, syote):
        self.sovellus = sovellus
        self.syote = syote

    def suorita(self):
        self.sovellus.plus(int(self.syote()))

class Erotus:
    def __init__(self, sovellus, syote):
        self.sovellus = sovellus
        self.syote = syote

    def suorita(self):
        self.sovellus.miinus(int(self.syote()))

class Nollaus:
    def __init__(self, sovellus, syote):
        self.sovellus = sovellus
        self.syote = syote

    def suorita(self):
        self.sovellus.nollaa()

class Kumoa:
    def __init__(self, sovellus, syote):
        self.sovellus = sovellus
        self.syote = syote

    def suorita(self):
        self.sovellus.aseta_arvo(self.sovellus.edellinen)