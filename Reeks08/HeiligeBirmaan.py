def kleur(genotype):
    '''
    >>> kleur('CcDd')
    'seal'
    >>> kleur('ccdd')
    'lilac'
    '''
    if 'C' in genotype and 'D' in genotype:
        return 'seal'
    elif 'C' in genotype:
        return 'blue'
    elif 'D' in genotype:
        return 'chocolate'
    else: return 'lilac'
    
def combinaties(genotype):
    '''
    >>> combinaties('CcDd')
    ['CD', 'Cd', 'cD', 'cd']
    >>> combinaties('ccdd')
    ['cd', 'cd', 'cd', 'cd']
    '''
    i_lijst = [0,0,1,1]
    j_lijst = [2,3,2,3]
    return [genotype[i]+genotype[j]  for i,j in zip(i_lijst,j_lijst)]
    
def punnett(kat, kattin, pprint=False):
    '''
    >>> print(punnett('CcDd', 'CcDd'))
    [['CCDD', 'CCDd', 'CcDD', 'CcDd'], ['CCdD', 'CCdd', 'CcdD', 'Ccdd'], ['cCDD', 'cCDd', 'ccDD', 'ccDd'], ['cCdD', 'cCdd', 'ccdD', 'ccdd']]
    >>> print(punnett('CcDd', 'CcDd', pprint=True))
    CCDD CCDd CcDD CcDd
    CCdD CCdd CcdD Ccdd
    cCDD cCDd ccDD ccDd
    cCdD cCdd ccdD ccdd
    >>> print(punnett('cCDd', 'CcdD', pprint=True))
    cCDd cCDD ccDd ccDD
    cCdd cCdD ccdd ccdD
    CCDd CCDD CcDd CcDD
    CCdd CCdD Ccdd CcdD
    '''
    kat,kattin = combinaties(kat),combinaties(kattin)
    vierkant = [] 
    for p in kat:
        vierkant.append([p[0]+q[0]+p[1]+q[1] for q in kattin])
    if pprint:
        nieuwvierkant = ''
        for i in range(4):
            nieuwvierkant += ' '.join(vierkant[i])
            if i != 3:
                nieuwvierkant += '\n'
        return nieuwvierkant
    return vierkant  

def kleurverdeling(kat, kattin):
    '''
    >>> kleurverdeling('CcDd', 'CcDd') == {'blue': 3, 'seal': 9, 'lilac': 1, 'chocolate': 3}
    True
    >>> kleurverdeling('cCDD', 'cCDD') == {'seal': 12, 'chocolate': 4}
    True
    >>> kleurverdeling('ccDD', 'ccDD') == {'chocolate': 16}
    True
    >>> kleurverdeling('ccdd', 'CcDd') == {'blue': 4, 'lilac': 4, 'seal': 4, 'chocolate': 4}
    True
    ''' 
    vierkant = punnett(kat, kattin)
    ongenestvierkant = []
    for i, _ in enumerate(vierkant):
        ongenestvierkant.extend(vierkant[i])
    kleurlijst = [kleur(e) for e in ongenestvierkant]
    d = {}
    for k in kleurlijst:
        if k not in d:
            d[k] = 0
        d[k] += 1
    return d
        
    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()