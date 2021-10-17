#input 
a = int(input('a:'))
b = int(input('b:'))
n = int(input('n'))
t = int(input('t:'))
x = 1
sec = 0

#experiment 1
for i in range(n):
    x = a*x + b

#experiment 2   
while t < x:
    t = a*t + b
    sec += 1
    
#print  
print('experiment #1: {} cellen na {} seconden'.format(x,i))
print('experiment #2: {} cellen na {} seconden'.format(t, sec))