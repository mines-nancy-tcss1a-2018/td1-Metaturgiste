### Exercice 16 #####
print('Probleme 16')

def solve(n):
    return sum([int(i) for i in str(2**n)])

assert( solve(15) == 26 )

print(solve(10**3))


### Exercice 22 #####
print('Probleme 22')

f = open('names.txt', 'r')
for ligne in f :
    ligne = ligne.replace('"','')
    noms = ligne.split(',')
f.close()
noms.sort()

listeVals = []
nbNoms = len(noms)

for numNom in range(nbNoms) :
    nom = noms[numNom]
    nomVal = 0
    for chara in nom :
        nomVal += ord(chara) - 64
    listeVals.append(nomVal*(numNom+1))
solution = sum(listeVals)
print(solution)


### Exercice 55 #####
print('Probleme 55')

def iteration(nombre):
    liste = (list(str(nombre)))
    liste.reverse()
    erbmon = ''
    for chiffre in liste :
        erbmon += chiffre
    return int(erbmon)+nombre

def testPali(nombre):
    bool = True
    nombre = str(nombre)
    taille = len(nombre)//2
    for i in range(taille):
        if nombre[i] != nombre[-i-1]:
            bool = False
            break
    return(bool)

def testLy(nombre):
    nombre = iteration(nombre)
    i = 0
    while i<50 and testPali(nombre)==False :
        i += 1
        nombre = iteration(nombre)
    return(i==50)

def solution():
    nbLy = 0
    for nombre in range(10000):
        if testLy(nombre) == True :
            nbLy += 1
    return nbLy

print(solution())