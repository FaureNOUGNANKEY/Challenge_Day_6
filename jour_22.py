# Exercises: Day 22
# 1.
import requests
from bs4 import BeautifulSoup
import json
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    facts_section = soup.find('div', class_='facts-stats')
    data = {}
    for item in facts_section.find_all('div', class_='fact-item'):
        title = item.find('h3').get_text(strip=True)
        value = item.find('p').get_text(strip=True)
        data[title] = value
    with open('bu_facts.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Data successfully saved to bu_facts.json")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
# 2.
url = 'https://archive.ics.uci.edu/ml/datasets.php'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
datasets = []
for row in soup.find_all('table')[5].find_all('tr')[1:]:  
    cols = row.find_all('td')
    if len(cols) >= 1:
        dataset = {
            'name': cols[0].get_text(strip=True),
            'link': 'https://archive.ics.uci.edu' + cols[0].find('a')['href'] if cols[0].find('a') else None
        }
        datasets.append(dataset)
with open('uci_datasets.json', 'w', encoding='utf-8') as f:
    json.dump(datasets, f, ensure_ascii=False, indent=4)
print("UCI datasets saved to uci_datasets.json")
# 3.
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', class_='wikitable')
presidents = []
for row in table.find_all('tr')[1:]:
    cols = row.find_all(['th', 'td'])
    if len(cols) >= 4:
        president = {
            'name': cols[0].get_text(strip=True),
            'term': cols[1].get_text(strip=True),
            'party': cols[2].get_text(strip=True),
            'portrait': cols[0].find('img')['src'] if cols[0].find('img') else None
        }
        presidents.append(president)
with open('us_presidents.json', 'w', encoding='utf-8') as f:
    json.dump(presidents, f, ensure_ascii=False, indent=4)
print("US presidents saved to us_presidents.json")