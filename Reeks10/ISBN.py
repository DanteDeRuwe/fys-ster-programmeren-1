
    
class ISBN13:
    '''
    >>> code = ISBN13(9780136110675)
    >>> print(code)
    978-0-13611067-5
    >>> code
    ISBN13(9780136110675, 1)
    >>> code.isGeldig()
    True
    >>> code.alsISBN10()
    '0-13611067-3'
    '''
    def __init__(self, code, landlen=1):
        assert isinstance(landlen, int) and landlen in range(1,6), 'fout'
        self.code = code
        self.landlen = landlen
    def __str__(self):
        return str(self.code)[:3] + '-' + str(self.code)[3:3+self.landlen] + '-' + str(self.code)[3+self.landlen:-1] + '-' + str(self.code)[-1]
    def __repr__(self):
        return 'ISBN13({}, {})'.format(self.code,self.landlen)
    
    def isGeldig(self):
        code = str(self.code)
        if not code.isdigit() or len(code) != 13 or ( code[:3] not in {'978', '979'} ) :
            return False 
        controle = (10 - (sum([int(code[i]) for i in range(12)]) + 2 * sum([int(code[2*j+1]) for j in range(6)]))%10)%10
        return controle == int(code[-1])
    
    def alsISBN10(self):
        if not self.isGeldig or not str(self.code).startswith('978'):
            return None 
        else:
            code = str(self.code)[3:-1]
        controle = sum((i + 1) * int(code[i]) for i in range(9)) % 11
        controle = 'X' if controle == 10 else str(controle)
        return code[:self.landlen] + '-' + code[self.landlen:] + '-' + str(controle)
        
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())