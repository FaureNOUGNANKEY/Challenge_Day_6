# 💻 Exercises: Day 7
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Exercises: Level 1
# 1. length of the set it_companies
print (len(it_companies))
# 2.Add 'Twitter' to it_companies
it_companies.add('Twitter')
# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['WhatsApp','SISCO','Lenovo'])
# 4.Removing one of the companies from the set it_companies
it_companies.remove('Twitter')
# 5.difference between remove and discard 
# la methode revome() produit une erreur si l'element qu'on veut supprimé n'existe pas contrairement à la méthode discard() qui ne produit pas d'erreur 

# Exercises: Level 2
# 1. Join A and B
A.update(B)
# 2. Finding A intersection B
print (A.intersection(B))
# 3. yes A is a subset of B
print (A.issubset(B))
# 4.No A and B are not a disjoint sets
print (A.isdisjoint(B))
# 5.
A_join_B = A.union(B)
B_join_A = B.union(A)
# 6. the symmetric difference between A and B is an empty set 
# 7.deteting the sets 
del A,B,it_companies

# Exercises: Level 3
set_age = set(age)
print("Taille de la liste :", len(age))
print("Taille du set :", len(set_age))
# the list is bigger than the set 
# 2.
# -un string est une suite de caractères entre guillemets et qui est non modifiable 

# - une liste est une collection ordonnée et modifiable d’éléments

# - un tuple est une liste non modifiable une fois créée

# -un set est un ensemble non ordonnée et sans doublons d'emement.
# 3.
sentence = "I am a teacher and I love to inspire and teach people"
# there ten (10) unique words in the sentence 
lt_sentence = sentence.split()
set_sentence = set(lt_sentence)
print (set_sentence)