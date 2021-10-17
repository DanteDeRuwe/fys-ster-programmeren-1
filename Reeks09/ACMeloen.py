def patroon(woord):
    '''
    >>> patroon('AC Meloen')
    '_C M_l__n'
    >>> patroon('woestijnvis')
    'w__st_jnv_s'
    >>> patroon('bruudruuster')
    'br__dr__st_r'
    '''
    output = ''
    for l in woord:
        if l.lower() in {'a','e','i','o','u',}:
            output += '_'
        else:
            output += l
    return output

def blunders(bestand, lengte=1, voorkomens=1):
    '''
    >>> mogelijkheden = blunders('radvanfortuin.txt')
    >>> mogelijkheden['_C M_l__n'] == {'AC Meloen', 'AC Milaan'}
    True
    >>> mogelijkheden['w__st_jnv_s'] == {'woestijnvos', 'woestijnvis'}
    True
    >>> mogelijkheden['br__dr__st_r'] == {'broodrooster', 'bruudruuster'}
    True
    >>> blunders('radvanfortuin.txt', lengte=12) == {'br__dr__st_r': {'bruudruuster', 'broodrooster'}, 'B_ll Cl_nt_n': {'Bill Clinton'}, 'J_ll Cl_nt_n': {'Jill Clinton'}}
    True
    >>> blunders('radvanfortuin.txt', voorkomens=3) == {'p_mp_lm__s': {'pimpelmees', 'pompelmoes', 'pimpelmuis'}, '_s_b_ll_ _': {'Osebolle O', 'Asebille O', 'Isabelle A'}}
    True
    >>> blunders('radvanfortuin.txt', voorkomens=2, lengte=12) == {'br__dr__st_r': {'broodrooster', 'bruudruuster'}}
    True
    '''
    d = {}
    bestand = open(bestand, 'r')
    for woord in bestand:
        woord = woord.rstrip('\n')
        if patroon(woord) not in d:
            if len(patroon(woord)) >= lengte or lengte == 1:
                d[patroon(woord)] = {woord}
        else: 
            if len(patroon(woord)) >= lengte or lengte == 1:
                d[patroon(woord)].add(woord)
    bestand.close()
    if voorkomens != 1:
        newd = {nd:d[nd] for nd in d if len(d[nd]) >= voorkomens}
        return newd
    else: return d
    
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())