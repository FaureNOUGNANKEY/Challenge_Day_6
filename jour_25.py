# Exercises: Day 25
# 1.
import pandas as pd
import numpy as np
df = pd.read_csv('./data/hacker_news.csv')
# 2.
print (df.head())
# 3.
print (df.tail())
# 4.
title = df['title']
print (title)
# 5.
print (df.shape)
# ..
python_mask = df['title'].str.contains('python', case=False, na=False)
python_titles = df[python_mask]
print(python_titles)
# ..
js_mask = df['title'].str.contains('javascript',case=False , na=False)
javascript_titles = df[js_mask]
print (javascript_titles)
# ..
# Count how many titles mention Python or JavaScript
print("Python mentions:", python_mask.sum())
print("JavaScript mentions:", js_mask.sum())
# Titles that mention both
both_mask = python_mask & js_mask
both_titles = df[both_mask]
print("Titles mentioning both:", both_titles)
# Titles that mention Python but not JavaScript
python_only = df[python_mask & ~js_mask]
print("Python only titles:", python_only)
print (df)
# Titles that mention JavaScript but not Python
js_only = df[js_mask & ~python_mask]
print("Python only titles:", js_only)


