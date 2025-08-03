# 💻 Exercises: Day 12
# Exercises: Level 1
# 1.
import random
import string
def random_user_id():
    strings = string.ascii_letters + string.digits
    return ''.join(random.choices(strings, k=6))

# 2.
def user_id_gen_by_user():
    length = int(input("Nombre de caractères par ID : "))
    count = int(input("Nombre d'IDs à générer : "))
    characters = string.ascii_letters + string.digits
    ids = []
    for i in range(count):
        ids.append(''.join(random.choices(characters, k=length)) )
    return '\n'.join(ids)
print(user_id_gen_by_user())
# 3.
def rgb_color_gen():
    return (f"rgb({random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)})")
# Exercises: Level 2
# 1.
def list_of_hexa_colors(n):
    colors = []
    heza = string.digits + 'A'+'B'+'C'+'D'+'E'+'F'
    for i in range(n):
        colors.append('#'+''.join(random.choices(heza, k=6)) )
    return colors
print (list_of_hexa_colors(6))
# 2.
def list_of_rgb_colors(n):
    rgb = []
    for i in range (n):
        rgb.append(rgb_color_gen())
    return rgb
# 3.
def generate_colors(type, n):
    if type == 'hexa':
        return list_of_hexa_colors(n)
    elif type == 'rgb':
        return list_of_rgb_colors(n)
    else:
        return "Type invalide. Utilisez 'hexa' ou 'rgb'."

# Exercises: Level 3
# 1.
def shuffle_list(lst):
    shuffled = lst[:]  
    random.shuffle(shuffled)
    return shuffled
# 2.
def unique_random_numbers():
    return random.sample(range(10), 7)

print(unique_random_numbers())  