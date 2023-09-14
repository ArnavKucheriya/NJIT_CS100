list_Pets = ['Dog', 'Cat', 'Bird', 'Fish', 'Hamster', 'Snake', 'Lizard', 'Turtle', 'Rabbit', 'Frog']
list_Nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list_Pets)
print(list_Nums)

# Accessing elements in a list
print('Printing Index 0 of List Pets:',list_Pets[0])
print('Printing Index 6 of List Pets:',list_Pets[6])

# Accessing elements in a list using negative indices
print('Printing the last value of List Pets:',list_Pets[-1])
print('Printing the second to last value of List Pets:',list_Pets[-2])

# Slicing a list
print('Printing the first 3 values of List Pets:',list_Pets[:3])
print('Printing the last 3 values of List Pets:',list_Pets[-3:])

# Slicing a list with a step
print('Printing every 2nd value of List Pets:',list_Pets[::2])

# Slicing a list with a negative step
print('Printing every 2nd value of List Pets in reverse:',list_Pets[::-2])

'''
Binary Numbers:
000 = 0
001 = 1
010 = 2
011 = 3
100 = 4
101 = 5
110 = 6
111 = 7

0101 = 1*2^0 + 0*2^1 + 1*2^2 + 0*2^3 = 1 + 0 + 4 + 0 = 5
'''