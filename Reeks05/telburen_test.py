layout = list(input('layout'))
nummer = list(str(input('nummer')))
layposlijst = []
for i, element in enumerate(layout):
    if element.isdigit():
        layposlijst.append(i) #lijst met alle posities in de layout waar cijfers staan
verschil = len(nummer) - len(layposlijst)
print('verschil', verschil)
if verschil < 0:
    nummer = abs(verschil) * ['0'] + nummer
    print('na nullen:', nummer)
for j, pos in enumerate(layposlijst):
    layout[pos] = nummer[j]
print(''.join(layout))