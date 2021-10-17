class Lemming:
    '''
    >>> lemming = Lemming('level.txt', 3, '<')
    >>> lemming.positie()
    (3, 3, '<')
    >>> print(lemming)
    #################################
    #                               #
    #         #                     #
    #  <    ###                     #
    ###########      ###            #
    ###########    ########         #
    ###########  ##############     #
    #################################
    >>> lemming.stap()
    (3, 2, '<')
    >>> lemming.stap()
    (3, 1, '<')
    >>> lemming.stap()
    (3, 1, '>')
    >>> lemming.stap()
    (3, 2, '>')
    >>> print(lemming)
    #################################
    #                               #
    #         #                     #
    # >     ###                     #
    ###########      ###            #
    ###########    ########         #
    ###########  ##############     #
    #################################
    >>> lemming.stappen(5)
    [(3, 3, '>'), (3, 4, '>'), (3, 5, '>'), (3, 6, '>'), (3, 7, '>')]
    >>> print(lemming)
    #################################
    #                               #
    #         #                     #
    #      >###                     #
    ###########      ###            #
    ###########    ########         #
    ###########  ##############     #
    #################################
    >>> lemming.stap()
    (2, 8, '>')
    >>> print(lemming)
    #################################
    #                               #
    #       > #                     #
    #       ###                     #
    ###########      ###            #
    ###########    ########         #
    ###########  ##############     #
    #################################
    >>> lemming.stap()
    (2, 9, '>')
    >>> lemming.stap()
    (1, 10, '>')
    >>> print(lemming)
    #################################
    #         >                     #
    #         #                     #
    #       ###                     #
    ###########      ###            #
    ###########    ########         #
    ###########  ##############     #
    #################################
    >>> lemming.stap()
    (6, 11, '>')
    >>> print(lemming)
    #################################
    #                               #
    #         #                     #
    #       ###                     #
    ###########      ###            #
    ###########    ########         #
    ###########> ##############     #
    #################################
    >>> lemming.stappen(21)
    [(6, 12, '>'), (5, 13, '>'), (5, 14, '>'), (4, 15, '>'), (4, 16, '>'), (3, 17, '>'), (3, 18, '>'), (3, 19, '>'), (4, 20, '>'), (4, 21, '>'), (4, 22, '>'), (5, 23, '>'), (5, 24, '>'), (5, 25, '>'), (5, 26, '>'), (6, 27, '>'), (6, 28, '>'), (6, 29, '>'), (6, 30, '>'), (6, 31, '>'), (6, 31, '<')]
    >>> lemming.stappen(21)
    [(6, 30, '<'), (6, 29, '<'), (6, 28, '<'), (6, 27, '<'), (5, 26, '<'), (5, 25, '<'), (5, 24, '<'), (5, 23, '<'), (4, 22, '<'), (4, 21, '<'), (4, 20, '<'), (3, 19, '<'), (3, 18, '<'), (3, 17, '<'), (4, 16, '<'), (4, 15, '<'), (5, 14, '<'), (5, 13, '<'), (6, 12, '<'), (6, 11, '<'), (6, 11, '>')]
    >>> print(lemming)
    #################################
    #                               #
    #         #                     #
    #       ###                     #
    ###########      ###            #
    ###########    ########         #
    ###########> ##############     #
    #################################
    '''
    
    def __init__(self, levelbestand, dropkolom, beginrichting):
        levelbestand = open(levelbestand, 'r')
        level = [list(k) for k in [r.rstrip() for r in levelbestand]]
        
        for i,l in enumerate(level[1:]): #nulde rij nooit controleren
            if l[dropkolom] is '#':
                level[i][dropkolom] = beginrichting #level[i] is de rij boven de gecontroleerde rij, want door de slice tellen we anders
                break
        self.level = level
    
    def __str__(self):
        return '\n'.join([''.join(r) for r in self.level])
    
    def positie(self):
        for i,r in enumerate(self.level[1:]): #nulde rij nooit controleren
            if '<' in r:
                return (i+1, r.index('<'), '<')
            elif '>' in r:
                return (i+1, r.index('>'), '>')
    
    def stap(self):
        r,k, richt = self.positie()[0] , self.positie()[1], self.positie()[2] 
           
        #voor bewegingen naar links
        if richt == '<':
            self.level[r][k] = ' ' #verwijder de oorspronkelijke pijl
            
            if self.level[r][k-1] == '#' and self.level[r-1][k-1] == '#' :
                richt = '>'
            
            else: #als we sowieso door kunnen
                
                #kolomindex aanpassen
                k -= 1 
                
                #rijindex als springen
                if self.level[r][k] == '#':
                    r -= 1
                #rijindex als vallen
                while self.level[r][k] == ' ': #als leegte
                    r += 1
                #nu we grond hebben gevonden, zetten we de lemming erop
                r -= 1
        
        #voor bewegingen naar rechts
        elif richt == '>':
            self.level[r][k] = ' ' #verwijder de oorspronkelijke pijl
            
            
            if self.level[r][k+1] == '#' and self.level[r-1][k+1] == '#' :
                richt = '<'
            
            else: #als we sowieso door kunnen
                
                #kolomindex aanpassen
                k += 1 
                
                #rijindex als springen
                if self.level[r][k] == '#':
                    r -= 1
                #rijindex als vallen
                while self.level[r][k] == ' ': #als leegte
                    r += 1
                #nu we grond hebben gevonden, zetten we de lemming erop
                r -= 1
              
        self.level[r][k] = richt #nieuw pijltje plaatsen
        return (r, k, richt)     #tuple teruggeven
        
    def stappen(self, aantal):
        return [self.stap() for _ in range(aantal)]
            
from time import sleep
import os


lemming = Lemming('level.txt', 9, '<')

for _ in range(200):
    lemming.stap()
    print(lemming)
    sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
t = input('press to exit')
    