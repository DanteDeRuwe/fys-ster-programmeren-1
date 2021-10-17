def complement(base):
    d = {'G':'C', 'C':'G', 'A':'T', 'T':'A'}
    return d[base]

def omgekeerdComplement(streng):
    '''
    >>> omgekeerdComplement('GATATC')
    'GATATC'
    >>> omgekeerdComplement('GCATGC')
    'GCATGC'
    >>> omgekeerdComplement('AGCTTC')
    'GAAGCT'
    '''
    streng = streng[-1::-1]
    compl = ''
    for base in streng:
        compl += complement(base)
    return compl

def omgekeerdPalindroom(streng):
    """
    >>> omgekeerdPalindroom('GATATC')
    True
    >>> omgekeerdPalindroom('GCATGC')
    True
    >>> omgekeerdPalindroom('AGCTTC')
    False
    """
    return streng == omgekeerdComplement(streng)

def restrictieseqperlengte(streng, lengte):
    """
    >>> restrictieseqperlengte('AAGTCATAGCTATCGATCAGATCAC', 8)
    [(6, 'ATAGCTAT')]
    >>> restrictieseqperlengte('TCAATGCATGCGGGTCTATATGCAT', 6)
    [(4, 'ATGCAT'), (6, 'GCATGC'), (20, 'ATGCAT')]
    """
    outputlijst = []
    for i,_ in enumerate(streng):
        kandidaat = streng[i:i+lengte]
        if omgekeerdPalindroom(kandidaat) and len(kandidaat) == lengte:
            outputlijst.append((i+1, omgekeerdComplement(kandidaat)))
    return outputlijst

def sorteren(lijst):
    """
    >>> sorteren([(7, 'TAGCTA'), (12, 'ATCGAT'), (6, 'ATAGCTAT')])
    [(6, 'ATAGCTAT'), (7, 'TAGCTA'), (12, 'ATCGAT')]
    """
    hoogsteindex = max([t[0] for t in lijst])
    nieuwelijst = []
    for i in range(1, hoogsteindex+1):
        nieuwelijst.extend([element for element in lijst if element[0] == i])
    return nieuwelijst    

def restrictieplaatsen(streng, minLengte = 4, maxLengte = 12):
    """
    >>> restrictieplaatsen('TCAATGCATGCGGGTCTATATGCAT')
    [(4, 'ATGCAT'), (5, 'TGCA'), (6, 'GCATGC'), (7, 'CATG'), (17, 'TATA'), (18, 'ATAT'), (20, 'ATGCAT'), (21, 'TGCA')]
    >>> restrictieplaatsen('AAGTCATAGCTATCGATCAGATCAC', minLengte=5)
    [(6, 'ATAGCTAT'), (7, 'TAGCTA'), (12, 'ATCGAT')]
    >>> restrictieplaatsen('ATATTCAGTCATCGATCAGCTAGCA', maxLengte=5)
    [(1, 'ATAT'), (12, 'TCGA'), (14, 'GATC'), (18, 'AGCT'), (20, 'CTAG')]
    """
    lijstje = []
    for lengte in range(minLengte, maxLengte + 1):
        if restrictieseqperlengte(streng, lengte):
            lijstje.extend(restrictieseqperlengte(streng, lengte))
    lijstje = sorteren(lijstje) if lijstje else  []
    return lijstje
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()