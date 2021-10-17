#driehoekige klok

class Klok:
    '''
    >>> klok = Klok(11, 3)
    >>> klok.lampen()
    ((1, 2, 2, 0, 3), 'G')
    >>> klok
    Klok(11, 3)
    >>> print(klok)
        G
       G G
      G G .
     . . . .
    G G G . .
    >>> klok.verzetUren()
    Klok(12, 3)
    >>> klok.lampen()
    ((0, 0, 0, 0, 3), 'R')
    >>> klok.verzetUren(11)
    Klok(23, 3)
    >>> klok.lampen()
    ((1, 2, 2, 0, 3), 'R')
    >>> print(klok)
        R
       R R
      R R .
     . . . .
    R R R . .
    >>> klok.verzetMinuten()
    Klok(23, 4)
    >>> klok.lampen()
    ((1, 2, 2, 0, 4), 'R')
    >>> klok.verzetMinuten(42)
    Klok(23, 46)
    >>> klok.lampen()
    ((1, 2, 3, 2, 4), 'R')
    >>> print(klok)
        R
       R R
      R R R
     R R . .
    R R R R .
    >>> klok.verzetMinuten(13)
    Klok(23, 59)
    >>> klok.lampen()
    ((1, 2, 3, 4, 5), 'R')
    >>> print(klok)
        R
       R R
      R R R
     R R R R
    R R R R R
    >>> klok.verzetMinuten()
    Klok(0, 0)
    >>> klok.lampen()
    ((0, 0, 0, 0, 0), 'G')
    >>> print(klok)
        .
       . .
      . . .
     . . . .
    . . . . .
    >>> klok.verzetUren(10).verzetMinuten(17)
    Klok(10, 17)
    >>> klok.lampen()
    ((1, 2, 0, 2, 5), 'G')
    >>> print(klok)
        G
       G G
      . . .
     G G . .
    G G G G G
    
    >>> Klok(42, 42)
    Traceback (most recent call last):
    AssertionError: ongeldig tijdstip
    '''
    
    def __init__(self, uren, minuten):
        assert all((isinstance(uren, int), isinstance(minuten, int), uren in range(24), minuten in range(60))), 'ongeldig tijdstip'
        self.uren = uren
        self.minuten = minuten
        self.kleur = 'R' if self.uren >= 12 else 'G'
        
    def __repr__(self):
        return 'Klok({}, {})'.format(self.uren, self.minuten)
    
    def lampen(self):
        minuten = (self.uren%12)*60 + self.minuten
        t = []
        #met behulp van gehele deling kijken hoeveel keer alles erin past
        for i in (360, 120, 30, 6, 1):
            t.append(minuten//i)
            minuten -= (minuten//i)*i
        return (tuple(t), self.kleur)
     
    def __str__(self):
        s = ''
        for i in range(5):
            aantallampen = self.lampen()[0][i]
            kleuren = (self.kleur + ' ')*aantallampen #een string van de kleuren, gescheiden met eens spatie
            regel = ' '*(4-i) + kleuren + '. '*(i+1 - aantallampen) #spaties ervoor en puntjes erachter
            s += regel.rstrip() + '\n'
        return str(s).rstrip()
    
    def verzetUren(self, u=1):
        self.uren = (self.uren + u)%24
        self.kleur = 'R' if self.uren >= 12 else 'G'
        return self
    
    def verzetMinuten(self, m=1):
        self.uren = (self.uren + m//60)%24
        m -= (m//60)*60
        self.minuten += m
        self.kleur = 'R' if self.uren >= 12 else 'G'
        
        #check nu of door dit toevoegen self.minuten niet te groot is geworden
        self.verzetUren(self.minuten//60)
        self.minuten -= (self.minuten//60)*60
        
        return self
    
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())