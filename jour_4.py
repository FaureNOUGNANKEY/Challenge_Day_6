# EXERCICES -Day 4
# 1.
single_string = 'Thirty' + ' ' + 'Days' + ' ' + 'of' + ' '+ 'Python'
print (single_string)
# 2.
a = 'Coding'
b = 'For'
c = 'all'
space = ' '
string_concatenate = a + space + b + space + c 
print (string_concatenate)
# 3.
company = "Coding For All"
# 4.
print (company)
# 5.
print (len(company))
# 6.
company_upper = company.upper()
# 7.
company_lower = company.lower()
# 8.
print (company.capitalize())
print (company.title())
print (company.swapcase())
# 9.
first_word = company[0:company.find(" ")]
print (first_word)
# 10.
print (company.index("Coding"))
print (company.find("Coding"))
# 11.
print (company.replace("Coding" , "Python"))
# 12.
chaine = "Python for Everyone"
print (chaine.replace(chaine , "Python for all"))
# 13.
company_split = company.split()
print (company_split)
# 14.
string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print (string.split(","))
# 15.
# the character is 'C'
# 16.
# the last index is 13 
# 17.
# the character at index 10 is ' '
# 18.
chaine = "Python For Everyone"
acronym1 = "".join([word[0] for word in chaine.split() ])
print (acronym1)
# 19.
company = "Coding For All"
acronym2 = "".join([word[0] for word in company.split() ])
print (acronym2)
# 20.
print ("Coding For all".index('C'))
# 21.
print ("Coding For all".index('F'))
# 22.
print ("Coding For all".rfind('l'))
# 23.
sentence = "You cannot end a sentence with because because because is a conjunction"
print (sentence.find("because"))
# 24.
print (sentence.rindex("because"))
# 25.
print (sentence[31:54])
# 26.
print (sentence.index('because'))
# 27.
print (sentence[31:54])
# 28. yes 
company = "Coding For All"
print (company.startswith("Coding"))
# 29. no 
company = "Coding For All"
print (company.endswith("Coding"))
# 30.
string30 = ' Coding For All '
print (string30.strip())
# 31.
# thirty_days_of_python 
# 32.
list = ['Django','Flask','Bottle','Pyramid','Falcon']
print (" ".join(list))
# 33.
print ("I am enjoying this challenge. \nI just wonder what is nest.")
# 34.
print ("Name \4 Age \t Country \t City \nAsabeneh \t250\t Finland\tHelsinki")
# 35.
radius = 10
area = 3.14 * radius ** 2
print ("the area of a circle with radius {radius} is {area}")
