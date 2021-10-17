import urllib.request
from bs4 import BeautifulSoup

def soupThisUrl(url):
    page = urllib.request.urlopen(url)
    page = page.read()
    soup = BeautifulSoup(page, "lxml")
    return soup

def ISBN13(code):
    if not code.isdigit() or len(code) != 13 or ( code[:3] not in {'978', '979'} ) :
            return False 
    controle = (10 - (sum([int(code[i]) for i in range(12)]) + 2 * sum([int(code[2*j+1]) for j in range(6)]))%10)%10
    return controle == int(code[-1])

def printBoekInfo(code):
    '''
    >>> printBoekInfo('9780136110675')
    Titel: The Practice of Computing using Python
    Auteurs: William F Punch, Richard Enbody
    Uitgever: Addison Wesley
    >>> printBoekInfo('9780136110678')
    Foutieve ISBN-13 code'''
    if ISBN13(code):
        url = 'http://isbndb.com/api/books.xml?access_key=ZFD8L2Z5&index1=isbn&value1=' + str(code)
        soup = soupThisUrl(url)
        titel, auteur, uitgever = soup.find('title').string, soup.find('authorstext').string, soup.find('publishertext').string
        if auteur.endswith(', '):
            auteur = auteur[:-2] #komma en spatie weg
        print('Titel:', titel)
        print('Auteurs:',auteur)
        print('Uitgever:', uitgever)
    else:
        print('Foutieve ISBN-13 code')


printBoekInfo('9780136110675')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
