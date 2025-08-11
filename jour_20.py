# Exercises: Day 20
# 1.
import requests
import requests
import re
from collections import Counter
url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(url)
text = response.text
words = re.findall(r'\b[a-z]+\b', text.lower())
word_counts = Counter(words)
top_10 = word_counts.most_common(10)
for word, count in top_10:
    print(f"{word}: {count}")
# 2.
import statistics
from collections import defaultdict
cats_api = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cats_api)
cats = response.json()
weights = []
lifespans = []
country_breeds = defaultdict(list)
for cat in cats:
    try:
        weight_range = cat['weight']['metric'].split(' - ')
        weight_values = list(map(float, weight_range))
        weights.append(statistics.mean(weight_values))
    except:
        pass
    try:
        life_range = cat['life_span'].split(' - ')
        life_values = list(map(float, life_range))
        lifespans.append(statistics.mean(life_values))
    except:
        pass
    origin = cat.get('origin', 'Unknown')
    breed = cat.get('name', 'Unknown')
    country_breeds[origin].append(breed)
print("Weight (kg):")
print("Min:", min(weights))
print("Max:", max(weights))
print("Mean:", statistics.mean(weights))
print("Median:", statistics.median(weights))
print("Std Dev:", statistics.stdev(weights))

# ii.
print("\nLifespan (years):")
print("Min:", min(lifespans))
print("Max:", max(lifespans))
print("Mean:", statistics.mean(lifespans))
print("Median:", statistics.median(lifespans))
print("Std Dev:", statistics.stdev(lifespans))

#iii.
print("\nCountry and Breeds:")
for country, breeds in country_breeds.items():
    print(f"{country}: {len(breeds)} breeds")
# 3.
countries_api = 'https://restcountries.com/v3.1/all'
response = requests.get(countries_api)
countries = response.json()
# i. Largest countries 
largest = sorted(countries, key=lambda x: x.get('area', 0), reverse=True)[:10]
print("10 Largest Countries:")
for c in largest:
    print(f"{c['name']['common']}: {c['area']} km²")
# ii. Most spoken languages
language_count = defaultdict(int)
for country in countries:
    langs = country.get('languages', {})
    for lang in langs.values():
        language_count[lang] += 1
most_spoken = sorted(language_count.items(), key=lambda x: x[1], reverse=True)[:10]
print("\n10 Most Spoken Languages:")
for lang, count in most_spoken:
    print(f"{lang}: spoken in {count} countries")

# iii. Total number of unique languages
print("\nTotal Unique Languages:", len(language_count))

# 4.
from bs4 import BeautifulSoup
import requests

url = 'https://archive.ics.uci.edu/ml/datasets.php'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
print (soup)

