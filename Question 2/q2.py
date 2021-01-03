# Write regex to catch date format, (For example 2018-10-12, 2019/01/02, 2016.02.03, ...) as accurately as possible.

import re

# Setting some test strings with different date formats
x = '2018-10-12' 
y = '2019/01/02'
z = '2016.02.03'
a = '2016:01:11'


# Using a number group, followed by a non letter character pattern which repeated 3 times, to catch any delimiters used for datetime strings.
x_date = re.search('[\d]+\W[\d]+\W[\d]+',x)
print(f'datetime format from string x : {x_date.group(0)}')

y_date = re.search('[\d]+\W[\d]+\W[\d]+',y)
print(f'datetime format from string y : {y_date.group(0)}')

z_date = re.search('[\d]+\W[\d]+\W[\d]+',z)
print(f'datetime format from string z : {z_date.group(0)}')

a_date = re.search('[\d]+\W[\d]+\W[\d]+',a)
print(f'datetime format from string a : {a_date.group(0)}')


# Regular expression string = '[\d]+\W[\d]+\W[\d]+'
