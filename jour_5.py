# EXERCICES Day 5
# level 1
# 1.
list_vide = []
# 2.
list = [21,'lomé',3.14,'bonjour','chat',100]
# 3.
print (len(list))
# 4.
first_item = list[0]
middle_items = list[1:5]
last_item = list[-1]
print (first_item)
print (middle_items)
print (last_item)
# 5.
mixed_data_types = ['NOUGNANKEY',18,1.6 ,
4,'single','Dévego']
# 6.
it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
# 7.
print (it_companies)
# 8.
print (len(it_companies))
# 9.
first_companie = it_companies[0]
middle_companie = it_companies[3]
last_companie = it_companies[-1]
print (first_companie)
print (middle_companie)
print (last_companie)
# 10.
it_companies[1] = 'Whatsapp'
print (it_companies)
# 11.
it_companies.append("Lenovo")
# 12.
it_companies[3]= "dell"
# 13.
it_companies[0] = it_companies[0].upper()
print (it_companies)
# 14.
print ("#".join(it_companies))
# 15.
print ('IBM'in it_companies)
# 16.
it_companies.sort()
print (it_companies)
# 17.
it_companies.reverse()
print (it_companies)
# 18.
print (it_companies[:3])
# 19.
print (it_companies[-3:])
# 20.
print(it_companies[3])
# 21.
it_companies.pop(0)
# 22.
it_companies.pop(3)
# 23.
it_companies.pop()
# 24.
it_companies.clear()
# 25.
del (it_companies)
# 26.
front_end = ['HTML','CSS','JS','React','Redux']
back_end = ['Node','Express','MongoDB']
list_join = front_end + (back_end)
print (list_join)
# 27.
full_stack = list_join.copy()
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print (full_stack)

# LEVEL 2
# 1.
# .
ages = [19,22,19,24,20,25,26,24,25,24]
ages.sort()
print (max(ages))
print (min(ages))
# .
ages.append(min(ages))
ages.append(max(ages))
# .
ages.sort()
median = (ages[5] + ages[6])/2
print (median)
# .
average_age = sum(ages)/len(ages)
print (average_age)
# .
range_age = max(ages) - min(ages)
print (range_age)
# .
diff_min = abs(min(ages) - average_age)
diff_max = abs(max(ages) - average_age)
print("abs(min - average_age):", diff_min)
print("abs(max - average_age):", diff_max)
# 1.
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

print (countries[1:192])
# 2.
half_1 = countries[:(len(countries)//2+1)]
half_2 = countries[(len(countries)//2)+1:]
print (half_1)
print (half_2)
# 3.
countries_s = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
scandic_countries = countries_s[:3]
unscandic_countries = countries_s[3:]
