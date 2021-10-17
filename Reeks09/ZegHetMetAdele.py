
def mix(txt1, txt2, outputtxt=None):
    '''
    >>> mix('tom_waits.txt', 'adele.txt')
    Operator, number, please
    -->Hello from the other side<--
    It's been so many years
    -->I must have called a thousand times<--
    Will she remember my old voice
    -->To tell you I'm sorry for everything that I've done<--
    While I fight the tears?
    -->But when I call you never seem to be home<--
    
    >>> mix('tom_waits.txt', 'adele.txt', 'mix.txt')
    >>> print(open('mix.txt', 'r').read(), end='')
    Operator, number, please
    -->Hello from the other side<--
    It's been so many years
    -->I must have called a thousand times<--
    Will she remember my old voice
    -->To tell you I'm sorry for everything that I've done<--
    While I fight the tears?
    -->But when I call you never seem to be home<--'''
    
    txt1, txt2 = open(txt1, 'r'), open(txt2, 'r')
    if not outputtxt:
        for r1, r2 in zip(txt1, txt2):
            print(r1.rstrip('\n'))
            print('-->' + r2.rstrip('\n') + '<--')
    else:
        outputtxt = open(outputtxt, 'w')
        for r1, r2 in zip(txt1, txt2):
            print(r1.rstrip('\n'), file=outputtxt)
            print('-->' + r2.rstrip('\n') + '<--', file=outputtxt)
        outputtxt.close()
    txt1.close()
    txt2.close()
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()