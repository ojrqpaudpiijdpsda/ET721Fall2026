'''
Lab 4: loops and conditional statement
Jiaxi Pang
Sep 14, 2026
'''


print('\n----- Example 1: ------')
#multi-statement
age = 17
if(age>18):
    print('Go to AC/DC concert')
elif age == 18:
    print('go see pink floyd')
else:
    print('Go see Meatloaf')

print('Move on')

print('\n----- Example 2: ------')

annie = 1996
jane = 1999


if annie % 4 ==0:
    print('Annie wasnorn')
elif jane % 4 == 0:
    print('Jane was borin a leap year')
else:
    print('None of them were born in a leap year')

print('\n----- Example 3: ------')
age = int(input('Students age: '))
lunch = 'None'

if age<9:
    lunch = 'Milk'
elif age >= 10 and age <=14:
    lunch = "Sandwich"
elif age>=15 and age<=17:
    lunch = 'Burger'
else:
    lunch = 'out of range!'

print(f'At age {age} the food is {lunch}')

print('\n----- Example 4: ------')

for n in range(5,10):
    print(n, end ='\t')

print('Print from 3, 2, 1')
for m in range(3,0,-1):
    print(m, end = '\t')


print('\n----- Example 5: for loop in a list ------')
dates = [1982, 1980, 1973]
n = len(dates)

for year in dates:
    print(year)

for y in range(n):
    print(f'year {y} = {dates[y]}')

print('\n----- Example 6: for loop to access index and element------')
colors = ['red', 'yellow', 'purple', 'blue']
for i,c in enumerate(colors):
    print(i, c)

print('\n----- Example 7:while loop ------')
#use loop to check how many ratings is greater than or equal to 8 for list rating
ratings = [5, 7, 5, 8, 9, 6.2, 8.8,]
count = 0 
index = 0
lenratings = len(ratings)
while(index < lenratings):
    if ratings[index] >=8:
        count += 1

    index += 1
else:
    print(f'There is/are {count} good-excellent ratings')


print('\n----- Example 8: functions ------')
#define a function to add 1 to a number. The number is passed to the function as argument
def add(n):
    updated = n + 1
    print(f'{n} added 1 = {updated}')
    return updated

#call the function add
m = add(6)
print(f'Value of m = {m}')

print('\n----- Example 9: functions to pass strings ------')
#define a function concatenate two strings
def con(a,b):
    return(a + " - " + b)

#call function con
print(con('Bayside', 'Ny'))

print('\n ----- EXERCISE 1: Loops -----')
'''
given the list animals, create a new list with animals whose names are made of less than or equal 6 letters
put the animals that were grabbed into new animals
'''

animals = ['lion', 'giraffe', 'gorilla', 'parrots', 'crocodile', 'deer', 'swan']
newanimals = []


print('\n----- EXERCISE 2: FUNCTIONS ------')
#define a function to find and return the average of a grades in a list
grades = [65, 87, 95, 77, 35]

def average(list):
    lengthlist = len(list)
    for i in list:
        sum = 