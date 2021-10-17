def isISBN(code, isbn13 = True):
    """
    >>> isISBN('9789027439642', False)
    False
    >>> isISBN('9789027439642', True)
    True
    >>> isISBN('9789027439642')
    True
    >>> isISBN('080442957X')
    False
    >>> isISBN('080442957X', False)
    True
    """
    if not isinstance(code, str):
        return False
    
    if not isbn13:
        if not code[:-1].isdigit() or len(code) != 10:
            return False 
        controle = sum((i + 1) * int(code[i]) for i in range(9)) % 11
        controle = 'X' if controle == 10 else str(controle)
        return controle == code[-1]
    else:
        if not code.isdigit() or len(code) != 13:
            return False 
        controle = (10 - (sum([int(code[i]) for i in range(12)]) + 2 * sum([int(code[2*j+1]) for j in range(6)]))%10)%10
        return controle == int(code[-1])

def zijnISBN(lijst, isbn13 = None):
    '''
    >>> zijnISBN(
    ...     [
    ...         '0012345678', '0012345679', '9971502100', '080442957X',
    ...         5, True, 'The Practice of Computing Using Python',
    ...         '9789027439642', '5486948320146'
    ...     ]
    ... )
    [False, True, True, True, False, False, False, True, False]
    
    >>> zijnISBN(
    ...     [
    ...         '0012345678', '0012345679', '9971502100', '080442957X',
    ...         5, True, 'The Practice of Computing Using Python',
    ...         '9789027439642', '5486948320146'
    ...     ],
    ...     True
    ... )
    [False, False, False, False, False, False, False, True, False]
    
    >>> zijnISBN(
    ...     [
    ...         '0012345678', '0012345679', '9971502100', '080442957X',
    ...         5, True, 'The Practice of Computing Using Python',
    ...         '9789027439642', '5486948320146'
    ...     ],
    ...     False
    ... )
    [False, True, True, True, False, False, False, False, False]
        
    '''
    outputlijst = []
    for code in lijst:
        if isinstance(code, str):
            if isbn13 is None:
                if len(code) == 13:
                    outputlijst.append(isISBN(code, True))
                else:
                    outputlijst.append(isISBN(code, False))
            else:
                outputlijst.append(isISBN(code, isbn13))
        else:
            outputlijst.append(False)
    return outputlijst

if __name__ == '__main__':
    import doctest
    doctest.testmod()