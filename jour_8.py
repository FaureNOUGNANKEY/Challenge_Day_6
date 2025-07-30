# Exercises: Day 8
# 1.
dog = {}
# 2.
dog['name'] = 'police'
dog['color'] = 'black'
dog['breed'] = 'labrador'
dog['legs'] = 4
dog['age'] = 3
# 3.
student = {'first_name':'Faure','last_name':'NOUGNANKEY', 'gender':'Masculine', 'age':18,'marital_status':'single', 'skills':["Python", "CSS", "Excel"]
, 'country':'Togo', 'city':'lomé','address':'Dévégo'}
# 4.
print (len(student))
# 5.
skills_value = student['skills']
print (skills_value)
print (type(skills_value))
# 6.
student['skills'].append('Java')
student['skills'].append('Football')
# 7.
keys = student.keys()
print (keys)
# 8.
values = student.values()
print (values)
# 9.
lt_student = student.items()
print (lt_student)
# 10.
student.pop('last_name')
# 11.
del student

