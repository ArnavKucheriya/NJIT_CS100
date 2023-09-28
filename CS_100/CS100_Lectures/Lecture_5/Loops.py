

# For Loop Execution
word = "apple"
for letter in word:
    print(letter)
print()

# For loop in Tuple
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
for day in days:
    print(day)
print()

# For loop in list
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in number:
    print(num)
print()

'''
Creating an Infinite Loop

# For loop in list with functions
for i in number:
    number.append(i + 3)
    print('i =', i)
    print('number =', number)
'''

# For loop with Range
for i in range(len(number)):
    print(number[i])
print()

