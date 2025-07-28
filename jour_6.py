# EXERCICES: Day 6
# EXERCICES: LEVEL 1
# 1.
tpl = ()
# 2.
freres = ('Felix','Fernando','Flavien')
soeurs = ('Felicité','Fortunée')
# 3.
siblings = freres + soeurs
# 4. i have 5 siblings 
print (len(siblings))
# 5.
L_siblings = list(siblings)
L_siblings .append('Rémi')
L_siblings .append('Vicky')
family_members = tuple(L_siblings)

# EXERCICES: LEVEL 2
# 1.
siblings = family_members[:5]
parents = family_members[5:]
print (siblings)
print (parents)
# 2.
fruits = ("apple", "banana", "mango")
vegetables = ("carrot", "broccoli", "spinach")
animal_products = ("milk", "cheese", "eggs")
food_stuff_tp = fruits + vegetables + animal_products
# 3.
food_stuff_lt = list(food_stuff_tp)
# 4.
middle_items = food_stuff_tp[1:8]
print (middle_items)
# 5.
three_first_items = food_stuff_lt[:3]
three_last_items = food_stuff_lt[6:]
print (three_first_items)
print (three_last_items)
# 6.
del food_stuff_tp
# 7.
# ..
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway','Sweden')
print ('Denmark'in nordic_countries)
# ..
print ('Estonia' in nordic_countries)
# ..
print ('Iceland'in nordic_countries)