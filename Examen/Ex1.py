#POLKA DOT
 
def delen(reeks):
    '''
    >>> delen((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    [0, 2, 4, 6, 8, 10, 3, 7, 1, 9, 5]
    >>> delen([0, 8, 1, 6, 2, 10, 3, 7, 4, 9, 5])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> delen('ABCDEFGHIJKLMOP')
    ['A', 'C', 'E', 'G', 'I', 'K', 'M', 'P', 'D', 'H', 'L', 'B', 'J', 'F', 'O']
    >>> delen('ALBICODJEMFKGPH')
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P']
    '''

    #2 stapels maken
    reeks = list(reeks)
    nieuwereeks = []
    
    #hou bij of de vorige kaart gelegd werd of achteraan gestopt
    gelegd = False
    
    #blijf delen tot de stapel op is
    while reeks:
        if gelegd:
            reeks.append(reeks.pop(0)) #verijder de kaart en stop hem achteraan
            gelegd = False
        elif not gelegd:
            nieuwereeks.append(reeks.pop(0)) #verwijder de kaart en voeg hem toe aan een nieuwe stapel
            gelegd = True
    return nieuwereeks


def zoekvolgendestipindex(i, template):
    while template[i%len(template)] != '.':
        i = (i+1)%len(template)
    return i

def polka(reeks):
    '''
    >>> polka((0, 2, 4, 6, 8, 10, 3, 7, 1, 9, 5))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> polka([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [0, 8, 1, 6, 2, 10, 3, 7, 4, 9, 5]
    >>> polka('ACEGIKMPDHLBJFO')
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P']
    >>> polka('ABCDEFGHIJKLMOP')
    ['A', 'L', 'B', 'I', 'C', 'O', 'D', 'J', 'E', 'M', 'F', 'K', 'G', 'P', 'H']
    '''
    #werken met een lijst
    lijst = list(reeks)
    
    #maak een template met de eerste term van de lijst en puntjes als placeholders
    template = [lijst[0]] + ['.']*(len(lijst)-1)
    i = 0
    
    for cijfer in lijst[1:]:
        if template.count('.') >= 2:
            
            #zoek een stip, neem 1 positie verder, en zoek de volgende stip
            i = zoekvolgendestipindex(i, template)
            i = (i+1)%len(template)
            i = zoekvolgendestipindex(i, template)
            
            template[i] = cijfer
            
        elif template.count('.') == 1:
            template[template.index('.')] = cijfer
            
    return template
        
    
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())