def samenvoegen(reeks1, reeks2):
    """
    >>> samenvoegen(('A', 'B', 'C'),  [1, 2, 3])
    ['A', 1, 'B', 2, 'C', 3]
    >>> samenvoegen(['A'], [1, 2, 3, 4])
    ['A', 1]
    >>> samenvoegen(('A', 'B'),  (1, 2, 3, 4))
    ['A', 1, 'B', 2]
    >>> samenvoegen(('A', 'B', 'C'),  [1, 2])
    ['A', 1, 'B', 2]
    """
    reeks1 = list(reeks1)
    reeks2 = list(reeks2)
    outputlijst = []
    for x1, x2 in zip(reeks1, reeks2):
        outputlijst.extend((x1,x2))
    return outputlijst

def weven(reeks1, reeks2):
    """
    >>> weven(('A', 'B', 'C'),  [1, 2, 3])
    ['A', 1, 'B', 2, 'C', 3]
    >>> weven(['A'], [1, 2, 3, 4])
    ['A', 1, 'A', 2, 'A', 3, 'A', 4]
    >>> weven(('A', 'B'),  (1, 2, 3, 4))
    ['A', 1, 'B', 2, 'A', 3, 'B', 4]
    >>> weven(('A', 'B', 'C'),  [1, 2])
    ['A', 1, 'B', 2, 'C', 1]
    """
    reeks1 = list(reeks1)
    reeks2 = list(reeks2)
    outputlijst = []
    for i in range(max(len(reeks1), len(reeks2))): #i loopt tot alle elementen van de langste lijst uitgeput zijn
        outputlijst.extend((reeks1[i%len(reeks1)], reeks2[i%len(reeks2)])) 
        #modulo zorgt voor cyclisch karakter
    return outputlijst

def ritsen(reeks1, reeks2):
    """
    >>> ritsen(('A', 'B', 'C'),  [1, 2, 3])
    ['A', 1, 'B', 2, 'C', 3]
    >>> ritsen(['A'], [1, 2, 3, 4])
    ['A', 1, 2, 3, 4]
    >>> ritsen(('A', 'B'),  (1, 2, 3, 4))
    ['A', 1, 'B', 2, 3, 4]
    >>> ritsen(('A', 'B', 'C'),  [1, 2])
    ['A', 1, 'B', 2, 'C']
    """
    reeks1 = list(reeks1)
    reeks2 = list(reeks2)
    outputlijst = []
    for i in range(max(len(reeks1), len(reeks2))): #i loopt tot alle elementen van de langste lijst uitgeput zijn
        if i< len(reeks1): 
            outputlijst.append(reeks1[i]) 
        if i< len(reeks2): 
            outputlijst.append(reeks2[i]) 
    return outputlijst
if __name__ == '__main__':
    import doctest
    doctest.testmod()