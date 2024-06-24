numbers = [] # empty list


# adding numbers to this list
numbers.append(1) # adding 1 to the list
numbers.append(2) # adding 2 to the list
numbers.append(3) # adding 3 to the list
numbers.append(4) # adding 4 to the list
numbers.append(5) # adding 5 to the list
print(numbers)

#accessing the numbers in the list
print(numbers[0]) # prints the first number with index 0
print(numbers[2]) # prints the 3rd number with index 2
print(numbers[len(numbers)-1]) # prints the last number in the list

# deleting numbers from the list
num = numbers.pop() # removes the last number ->5
print(num)
print(numbers)
num = numbers.pop(1) #removes the number with index 1 -> 2
print(num)
print(numbers)
numbers.remove(3) # removes the number 3 from the list
print(numbers)

#for loop
for i in range(5):
    print(i) #prints the numbers from 0 to 4

for i in range(2,8):
    print(i)  # prints the numbers from 2 to 7

for i in range(3, 10, 2):
    print(i)  # prints the numbers from 3 to 10 skipping by 2

# adding numbers to the list using loops
numbers = []
for i in range(5):
    numbers.append(i)

#creating 2D list with nested loops
twoD = []
for i in range(3):
    for j in range(4):
        twoD.append([i,j])

print(twoD)
