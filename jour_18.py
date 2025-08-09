# 💻 Exercises: Day 18
# Exercises: Level 1
# 1.
import re 
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
# the most frequent word in this paragraph is 'love'
from collections import Counter
mots = re.findall(r'\w+', paragraph.lower())
frequences = Counter(mots)
for mot, count in frequences.most_common():
    print(f"{mot}: {count}")
print ("the most frequent word is ",frequences.most_common(1)[0])
# 2.
sentence = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction." 
points = re.findall(r'-?\d+',sentence)
points = [int(i) for i in points]
sorted_points = sorted(points)
distance = sorted_points[-1] - sorted_points[0]
print (distance)
# Exercises: Level 2
# 1.
def is_valid_variable(name):
    pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'
    return re.match(pattern, name) is not None
# Exercises: Level 3
# 1.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve
%tea@ching%;. There $is nothing; &as& mo@re rewarding as
educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching
m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s
mo@tivate yo@u to be a tea@cher!?'''
def clean_text(sentence):
    return re.sub('[%@$&#!;?]','',sentence)
cleaned_text = clean_text(sentence)
print (cleaned_text)

def most_frequent_words(text):
    words = text.split()  
    counte = Counter(words)  
    return counte.most_common(3)  
print (most_frequent_words(cleaned_text))