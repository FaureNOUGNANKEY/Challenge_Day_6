# 💻 Exercises: Day 16
# 1. 
from datetime import datetime
now = datetime.now()
current_day = now.day
current_month = now.month
current_year = now.year
current_hour = now.hour
current_minute = now.minute
timestamp = now.timestamp()
# 2.
print(f'{current_day}/{current_month}/{current_year}, {current_hour}:{current_minute}')
# 3.
date_string = '5 december, 2019'
date = datetime.strptime(date_string,"%d %B, %Y")
print (date)
# 4.
today = datetime(year = 2025, month = 8, day = 7)
new_year = datetime(year = 2026, month = 1, day = 1)
time_difference = new_year - today
print (time_difference)
# 5.
epoch = datetime(1917,1,1)
mow = datetime.now()
difference = now - epoch
print (difference)
# 6.
# date de publication d'un article 
def publier_article(titre):
    date = datetime.now().strftime("%d %B %Y à %H:%M")
    print(f"📢 Article publié : '{titre}' le {date}")

# etudier les visites sur un site 
dates = [datetime(2025, 1, 1), datetime(2025, 2, 1), datetime(2025, 3, 1)]
for date in dates:
    print("Point de données :", date.strftime("%d %B %Y"))