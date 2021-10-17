def ISBN13(code):
    if not code.isdigit() or len(code) != 13 or ( code[:3] not in {'978', '979'} ) :
            return False 
    controle = (10 - (sum([int(code[i]) for i in range(12)]) + 2 * sum([int(code[2*j+1]) for j in range(6)]))%10)%10
    return controle == int(code[-1])
def overzicht(codes):
    '''
    >>> codes = [
    ...    '9789743159664', '9785301556616', '9797668174969', '9781787559554',
    ...    '9780817481461', '9785130738708', '9798810365062', '9795345206033', 
    ...    '9792361848797', '9785197570819', '9786922535370', '9791978044523', 
    ...    '9796357284378', '9792982208529', '9793509549576', '9787954527409', 
    ...    '9797566046955', '9785239955499', '9787769276051', '9789910855708', 
    ...    '9783807934891', '9788337967876', '9786509441823', '9795400240705', 
    ...    '9787509152157', '9791478081103', '9780488170969', '9795755809220', 
    ...    '9793546666847', '9792322242176', '9782582638543', '9795919445653', 
    ...    '9796783939729', '9782384928398', '9787590220100', '9797422143460', 
    ...    '9798853923096', '9784177414990', '9799562126426', '9794732912038', 
    ...    '9787184435972', '9794455619207', '9794270312172', '9783811648340', 
    ...    '9799376073039', '9798552650309', '9798485624965', '9780734764010', 
    ...    '9783635963865', '9783246924279', '9797449285853', '9781631746260', 
    ...    '9791853742292', '9781796458336', '9791260591924', '9789367398012' 
    ... ]
    >>> overzicht(codes)
    Engelstalige landen: 8
    Franstalige landen: 4
    Duitstalige landen: 6
    Japan: 3
    Russischtalige landen: 7
    China: 8
    Overige landen: 11
    Fouten: 9 
    '''
    d = {'0':0,'1':0,'2':1,'3':2,'4':3, '5':4,'7':5, '6':6, '8':6, '9':6}
    counters = [0]*8
    for code in codes:
        if ISBN13(code):
            pos = d[code[3]]
            counters[pos] += 1
        else:
            counters[-1] += 1
    print('Engelstalige landen: {}\nFranstalige landen: {}\nDuitstalige landen: {}\nJapan: {}\nRussischtalige landen: {}\nChina: {}\nOverige landen: {}\nFouten: {} '.format(*counters))
    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()