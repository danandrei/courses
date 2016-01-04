class Multime:
    '''
    COLECTIE de numere întregi (asemănător mulţimii)

    Specificaţi şi implementaţi tipurile abstracte de date menţionate mai jos.
        La toate tipurile de date vor exista operaţii pentru:

        a) creare de valori din domeniul tipului respectiv;
        b) operaţii aritmetice
        c) comparare de valori
        d) extragere de componente
        e) eventual conversii din alte tipuri mentionate.
    '''
    def __init__(self, arr=[]):
        self.el = arr

    def getEl(self):
        return self.el

    def insert(self, x):
        if not self.find(x):
            self.el.append(x)

    def remove(self, x):
        if self.find(x):
            self.el = [y for y in self.el if x != y]

    def find(self, x):
        return x in self.el

    def len(self):
        return len(self.el)

    def __getitem__(self, item):
        return self.el[item]

    def __setitem__(self, key, value):
        self.el[key] = value

    def __add__(self, other):
        for x in other.el:
            if not self.find(x):
                self.insert(x)

    def __sub__(self, other):
        for x in other.el:
            if self.find(x):
                self.remove(x)