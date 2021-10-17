from fractions import gcd
class T52:
    '''
    >>> machine1 = T52(3, 5, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    >>> machine1.codeerSymbool('G')
    'X'
    >>> machine1.codeerSymbool('S')
    'H'
    >>> machine1.codeerSymbool('-')
    '-'
    
    >>> machine1.decodeerSymbool('X')
    'G'
    >>> machine1.decodeerSymbool('H')
    'S'
    >>> machine1.decodeerSymbool('-')
    '-'
    
    >>> machine1.codeer('G-SCHREIBER')
    'X-HLAERDIRE'
    >>> machine1.decodeer('X-HLAERDIRE')
    'G-SCHREIBER'
    
    >>> machine2 = T52(17, 11, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    >>> machine2.codeer('X-HLAERDIRE')
    'M-AQLBOKROB'
    
    >>> machine12 = machine1 + machine2
    >>> machine12.codeer('G-SCHREIBER')
    'M-AQLBOKROB'
    
    >>> T52(4, 5, 'ABCDEFGHIJKLMMLKJIHGFEDCBA')
    Traceback (most recent call last):
    AssertionError: alfabet bevat herhaalde symbolen
    
    >>> T52(4, 5, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    Traceback (most recent call last):
    AssertionError: 4 en 26 zijn niet copriem
    
    >>> machine1 + T52(17, 11, 'abcdefghijklmnopqrstuvwxyz')
    Traceback (most recent call last):
    AssertionError: alfabetten zijn verschillend
    '''
    
    def __init__(self, a, b, alfabet):
        m = len(alfabet)
        assert len(set(l for l in alfabet)) == m, 'alfabet bevat herhaalde symbolen'
        assert gcd(a, m) == 1, '{} en {} zijn niet copriem'.format(a,m)
        self.a = int(a)
        self.b = int(b)
        self.m = int(m)
        self.alfabet = str(alfabet)
        
    def __add__(self, other):
        assert self.alfabet == other.alfabet, 'alfabetten zijn verschillend'
        a = self.a * other.a
        b = other.a * self.b + other.b
        return T52(a,b, self.alfabet)
    
    def codeerSymbool(self, letter):
        
        x = self.alfabet.find(letter)
        
        if x == -1: #find geeft -1 terug bij een gefaalde zoekopdracht
            return str(letter)
        else:
            newindex = (self.a*x + self.b) % self.m
            return self.alfabet[newindex]
        
    def decodeerSymbool(self, letter):
        
        x = self.alfabet.find(letter)
        for i in range(self.m):
            if self.a*i % self.m == 1:
                a_accent = i
                break 
        
        if x == -1: #find geeft -1 terug bij een gefaalde zoekopdracht
            return str(letter)
        else:
            newindex = a_accent * (x - self.b) % self.m
            return self.alfabet[newindex]
        
    def codeer(self, woord):
        gecod = ''
        for l in woord:
            gecod += self.codeerSymbool(l)
        return gecod
    
    def decodeer(self, woord):
        gedecod = ''
        for l in woord:
            gedecod += self.decodeerSymbool(l)
        return gedecod
    
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())       