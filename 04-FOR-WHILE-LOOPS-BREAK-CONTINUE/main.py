# For Loop Example

# The range(start, stop) function generates numbers from start to stop - 1.
# This loop prints numbers from 1 to 5.

for number in range(1, 6):
    print(number)


# Print the multiplication table of 5
# This loop multiplies 5 by numbers from 1 to 10.

for multiplier in range(1, 11):
    product = 5 * multiplier
    print("5 x", multiplier, "=", product)


# While Loop Example

# This loop prints numbers from 1 to 5 using a while loop.

counter = 1

while counter <= 5:
    print(counter)
    counter = counter + 1


# Break Statement Example
# This loop prints numbers from 0 to 10 and stops when the number reaches 10.

for number in range(0, 21):
    print(number)
    if number == 10:
        break


# Continue Statement Example
# This loop prints numbers from 1 to 4 but skips the number 2.

for number in range(1, 5):
    if number == 2:
        continue
    print(number)
