# 💻 Exercises: Day 13
# 1.
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_numbers = [i for i in numbers if i<=0]
print (negative_numbers)
# 2.
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
fratten_list = [number for i in list_of_lists for j in i for number  in j]
print (fratten_list)
# 3.creating list of tuples 
tuple_list = [(i , 1 , i , i**2 , i**3 , i**4 , i**5)for i in range(11)]
print (tuple_list)
# 4.
countries = [[('Finland', 'Helsinki')], [('Sweden',
'Stockholm')], [('Norway', 'Oslo')]]
fratten_countries = [[country.upper(),country[:3].upper(),capital.upper()]for [(country,capital)] in countries]
print (fratten_countries)
# 5.
countries = [[('Finland', 'Helsinki')], [('Sweden',
'Stockholm')], [('Norway', 'Oslo')]]
list_of_dict = [{'country':country,'city':city}for [(country,city)] in countries ]
print (list_of_dict)
# 6.
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
[('Donald', 'Trump')], [('Bill', 'Gates')]]
list_of_concatenated_strings = [first_name + " " + last_name for [(first_name , last_name)] in names]
print (list_of_concatenated_strings)
# 7.
# lambda function to solve slope 
slope  = lambda  x, y, b: (y-b)/x
# lambda function to solve y_intercept
y_intercept = lambda m, x, y: y - m * x

