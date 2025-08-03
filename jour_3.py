# EXERCICE-Jour 3
# 1.
age = 18
# 2.
taille = 1.64
# 3.
x = 1+1j
# 4.
b = int(input(" Entrer la base: "))
h = int(input("Enter la hauteur: "))
print (f"la zone du triangle est de {0.5*b*h}")
# 5.
a = int (input("Entrez le coté A: "))
b = int (input("Entrez le coté B: "))
c = int (input("Entrez le coté C: "))
print (f"Le périmetre du triangle est {a+b+c}")
# 6.
longueur = float (input("Entrez la longueur du rectangle: "))
largeur = float (input("Entrez la largeur du rectangle: "))
surface = longueur * largeur
perimetre = 2*(longueur+largeur)
print (f"surface= {surface} ; périmetre= {perimetre}")
# 7.
pi = 3.14
r = float (input("Entrez la rayon du cercle: "))
zone = r*r*pi
c = 2*pi*r
print(f"zone= {zone} ; circonférence= {c}")
# 8.
pente = 2 
print ("la pente est: ",pente)
# 9.
x1 , y1 = 2 , 2
x2 , y2 = 6 , 10
m = (y2-y1)/(x2-x1)
print (f"la pente est {m}")
# 10.
if (pente == m ):
    print ("les pentes sont egaux")
else:
    print ("les pentes sont differents ")
# 11.

for i in range (20,-20,-1):
    x = i 
    y = x**2 + 6*x +9 
    print (y)
# pour x = -3 y =0 

# 12.
print ("la longueur de Python est ",len("Python"))
print ("la longueur de Dragon est ",len("Dragon"))
print (len("Python")!= len("Dragon"))
# 13.
if ("on" in "Python") and ("on" in "Dragon"):
    print (" 'on' se trouve dans python et dragon")
else :
    print (" 'on' ne se trouve pas dans python et dragon")
# 14.
phrase = "i hope this course is not full of jargon"
if ("jargon" in phrase):
    print ("jargon est dans la phrase")
else :
    print ("jargon n'est pas dans la phrase")
# 15.
print('on' in 'Dragon')  
print('on' in 'Python')  
# 16.
texte = "python"
longueur = len(texte)
en_float = float(longueur)
en_string = str(longueur)
# 17.
n = float(input("saisir le nombre"))
print (n%2==0)
# 18.
print (7/3 == int(2.7))  
# 19.
print (type(10)==type("10")) 
# 20.
print(int(9.8)==10)
# 21.
h = int (input ("Entrez les heures: "))
t = int (input ("Entrez le taux par heure: "))
print (f"votre gain hebdomadaire est de {h*t}")
# 22.
nb_annee = int (input("Entrez le nombre d'année que vous avez vécu: "))
print (f"Vous vivez pendant {nb_annee*31536000} secondes")
# 23.
print ("1 "*5)
for i in range (2,6):
    print (f"{i} {1} {i} {i**2} {i**3}")