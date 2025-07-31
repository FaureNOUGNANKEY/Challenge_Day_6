# Exercises: Day 9
# Exercises: Level 1
# 1.
age = int(input("Enter your age :"))
if (age >= 18):
    print ("You are old enough to learn to drive.")
else :
    print (f"You need {18-age} more years to learn to drive.")
# 2.
my_age = 18 
your_age = int (input("Enter your age :"))
if (your_age > my_age):
    print (f"you are {your_age - my_age} older than me")
elif (your_age < my_age):
    print (f"I am {my_age - your_age} older than you")
else :
    print ("we have the same age")
# 3.
a = int(input("Enter number one :"))
b = int(input("Enter number two :"))
if (a>b):
    print (f"{a} is greater than {b}")
elif (a<b):
    print (f"{a} is smaller than {b}")
else :
    print (f"{a} is equal to {b}")

# Exercises: Level 2
# 1.
score = int(input("Enter your score"))
if 80 <= score <= 100:
    print (f"your grade is {'A'}")
elif 70 <= score <= 79:
    print (f"your grade is {'B'}") 
elif 60 <= score <= 69:
    print (f"your grade is {'C'}") 
elif 50 <= score <= 59:
    print (f"your grade is {'D'}") 
elif 0 <= score <= 49:
    print (f"your grade is {'F'}")
# 2.
month = input("Enter the month")
if month =="September" or month == "October" or month== "Novenber":
    print ("the season is Autumn")
elif month =="December" or month == "January" or month== "February":
    print ("the season is Winter")
elif month =="March" or month == "April" or month== "May":
    print ("the season is Spring")
elif month =="June" or month == "July" or month== "August":
    print ("the season is Summer")
# 3.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input ("Enter the mane of the fruit")
if (fruit not in fruits):
    fruits.append(fruit)
else:
    print ("that fruit already exist in the list")

# Exercises: Level 3
# 1.
person = {
 'first_name': 'Asabeneh',
 'last_name': 'Yetayeh',
 'age': 250,
 'country': 'Finland',
 'is_marred': True,
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
 'address': {
 'street': 'Space street',
 'zipcode': '02210'
 }
 }
# *
if ('skills' in person.keys()):
    print ("the midle skill is",person['skills'][2])
# *
if ('skills' in person.keys()):
    print ('Python' in person['skills'])
# *
if (person['skills']==['JavaScript', 'React']):
    print ("he is a front end developer ")
elif (person['skills'] == ['Node', 'MongoDB', 'Python']):
    print ("he is backend developer")
elif (person['skills'] == ['React', 'Node', 'MongoDB']):
    print ("he is a fullstack developer")
else :
    print('unknown title')  
# *
if (person['is_marred'] == True and person['country']=="Finland"):
    print (f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
