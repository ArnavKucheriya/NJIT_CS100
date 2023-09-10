import numpy as np

msg = 'hello world, this is a test Python Program file.'
print(msg)

a = 10
b = 5
print('Value of a + b = ', a + b)

a = 'Changing the value of a to a String'
print(a)

print('Rolling a Dice!')
# Random Number Generator using Numpy (Pip installing numpy)
print(np.random.randint(1,9))

msg = 'hello world'
print(msg.capitalize())
print(msg.split('e'))

# Adding a orray to the program
array = np.array([1,2,3,4,5,6,7,8,9,10])

#Printing the array
print(array)

#Performing different operations on the array
print(array[0])
print(array[1:5])
print(array[5:])
print(array[:5])
print(array[-1])

for i in array:
    print(i)


   