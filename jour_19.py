# 💻 Exercises: Day 19
# Exercises: Level 1
# 1.
def count_lines(file):
    with open (file , 'r') as f :
        nb_word = 0 
        lines = f.readlines()
        for line in lines :
            for word in line :
                nb_word += 1
        return (f"there are {len(lines)} lines and {nb_word} words ")
# a.
print(count_lines('./data/obama_speech.txt'))    
# b.
print (count_lines('./data/michelle_obama_speech.txt'))  
# c.  
print (count_lines('./data/donald_speech.txt')) 
# d.   
print (count_lines('./data/melina_trump_speech.txt'))    
# 2.
import json
from collections import Counter

def most_spoken_languages(filename, n):
    with open(filename, 'r', encoding='utf-8') as file:
        countries = json.load(file)
    language_counter = Counter()
    for country in countries:
        for language in country.get('languages', []):
            language_counter[language] += 1
    most_common = language_counter.most_common(n)
    return most_common
print (most_spoken_languages('./data/countries_data.json',10))
# 3.
def most_populated_countries(filename, n):
    with open(filename, 'r', encoding='utf-8') as file:
        countries = json.load(file)
        populations = []
    for country in countries:
        populations.append ({'country':country['name'] ,'population':country['population']})
    sorted_population = sorted(populations, key=lambda x: x['population'],reverse=True)
    return sorted_population[:n]
print (most_populated_countries('./data/countries_data.json',10))
# Exercises: Level 2
# 4.
# 5.
import re
def find_most_common_words(text_or_file, n):
    try:
        with open(text_or_file, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        text = text_or_file
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    return word_counts.most_common(n)

