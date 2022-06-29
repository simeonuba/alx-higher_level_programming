import random
number = random.randint(-10000, 10000)
last_digit = int(repr(number)[-1])
print('last digit is', last_digit)

if last_digit > 5:
    print('is',last_digit,'and is greater than 5')
elif number == 0:
    print('is',last_digit,'and is 0')
else:
    print('is',last_digit,'iand is less than 6 and not 0')
