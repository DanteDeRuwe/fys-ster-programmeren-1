import math

class Blok:
    '''
    >>> rots = Blok(5, 2, 3)
    >>> rots
    Blok(lengte=5, hoogte=2, breedte=3, positie=(0, 0))
    >>> rots.oppervlakte()
    62.0
    >>> rots.volume()
    30.0
    >>> rots.diagonaal()
    6.164414002968976
    >>> rots2 = rots.schuif('R')
    >>> rots2
    Blok(lengte=5, hoogte=2, breedte=3, positie=(0, 5))
    >>> rots is rots2
    True
    >>> rots.schuif('V')
    Blok(lengte=5, hoogte=2, breedte=3, positie=(3, 5))
    >>> rots.kantel('L')
    Blok(lengte=2, hoogte=5, breedte=3, positie=(3, 3))
    >>> rots.kantel('A')
    Blok(lengte=2, hoogte=3, breedte=5, positie=(0, 3))
    >>> rots.kantel('A').schuif('L').kantel('L').schuif('A')
    Blok(lengte=5, hoogte=2, breedte=3, positie=(-8, -4))
    >>> rots.zeil('SA')
    Blok(lengte=5, hoogte=2, breedte=3, positie=(-11, -4))
    >>> rots.zeil('KR')
    Blok(lengte=2, hoogte=5, breedte=3, positie=(-11, 1))
    >>> rots.zeil('SVSVKLSLKAKASRSVKRKVKRKRSASV')
    Blok(lengte=2, hoogte=3, breedte=5, positie=(-2, 6))
    
    >>> rots.kantel('X')
    Traceback (most recent call last):
    AssertionError: ongeldige richting
    >>> rots.zeil('XY')
    Traceback (most recent call last):
    AssertionError: ongeldige beweging
    >>> rots.zeil('KY')
    Traceback (most recent call last):
    AssertionError: ongeldige richting
    '''
    def __init__(self, lengte, hoogte, breedte, positie=(0,0)):
        self.L = int(lengte)
        self.H = int(hoogte)
        self.B = int(breedte)
        self.pos = tuple(positie)
    
    def __repr__(self):
        return 'Blok(lengte={}, hoogte={}, breedte={}, positie={})'.format(self.L, self.H, self.B, tuple(self.pos) )
    
    
    def oppervlakte(self):
        return float(2*(self.L*self.B + self.L*self.H + self.H*self.B))
    
    def volume(self):
        return float(self.L*self.B*self.H)
    
    def diagonaal(self):
        return float(math.sqrt(self.L **2 + self.B **2 + self.H **2))


    def schuif(self, richting):
        pos = self.pos
        operaties = {'R': (0,self.L ), 'L': (0,-self.L), 'V': (self.B,0), 'A': (-self.B,0)}
        assert richting in operaties, 'ongeldige richting'
        
        newpos = []
        for p, o in zip(pos, operaties[richting]):
            newpos.append(p+o)
        
        self.pos = tuple(newpos) #positie van het nieuwe object wordt aangepast
        
        return self #functie geeft ge-input object weer terug, voor verdere berekeningen
    
    
    def kantel(self, richting):
        #nieuwe positie (idem werkwijze  als 'schuif', maar andere operaties)
        pos = self.pos
        operaties = {'R': (0, self.L ), 'L': (0,-self.H), 'V': (self.H,0), 'A': (-self.B,0)}
        assert richting in operaties, 'ongeldige richting'
        
        newpos = []
        for p, o in zip(pos, operaties[richting]):
            newpos.append(p+o)
        
        self.pos = tuple(newpos) #positie van het nieuwe object wordt aangepast
        #--------------------------------------------------------------------------
        
        #nieuwe L, B, H
        if richting in {'R', 'L'}:
            self.L, self.H = self.H, self.L #hoogte en lengte wisselen
        elif richting in {'V', 'A'}:
            self.B, self.H = self.H, self.B #breedte en hoogte wisselen
        
        return self             #functie geeft ge-input object weer terug, voor verdere berekeningen  
    
    
    def zeil(self, aanwijzingen):
        for i in range(0,len(aanwijzingen),2):
            assert aanwijzingen[i] in {'S', 'K'}, 'ongeldige beweging'
            if aanwijzingen[i] == 'S':
                self.schuif(aanwijzingen[i+1]) # aanwijzingen[i+1] is de richting voor het schuiven
            else:
                self.kantel(aanwijzingen[i+1]) # aanwijzingen[i+1] is de richting voor het kantelen
        
        return self
           
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())