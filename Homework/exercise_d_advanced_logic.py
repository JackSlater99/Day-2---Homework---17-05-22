# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

even_numbers = []

for i in numbers:
  if i % 2 == 0:
    even_numbers.append(i)
print(even_numbers)

# 2. Print the difference between the largest and smallest value:

big = max(numbers)
small = min(numbers)

difference = big - small
print(difference)

# 3. Print True if the list contains a 2 next to a 2 somewhere.

for i in range(0, len(numbers) - 1):
    if numbers[i + 1] == 2 and numbers[i] == 2:
        print(True)

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

has_six = False
sumo = 0

for i in numbers:
    if has_six:
        if i == 7:
            has_six = False
    else:
        if i == 6:
            has_six = True
        else:
            sumo += i

print(sumo)


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

total = 0
skip = False

for i in numbers:
    if skip:
        skip = False
        continue
    if i == 13:
        skip = True
        continue
    total += i

print(total)





