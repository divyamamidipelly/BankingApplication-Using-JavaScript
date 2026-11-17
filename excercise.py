''' 1. Program to add 2 numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum = a + b
print(sum)
'''
''' 2. Program to display quotient and remainder after division
a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))
quotient = a // b
remainder = a % b
print(quotient)
print(remainder)

'''

''' 3.Program to find the total and average of 3 numbers
a = int(input("Enter 1st number "))
b = int(input("Enter 2nd number"))
c = int(input("Enter 3rd number"))
total = a + b + c
average = total / 3
print(total)
print(average)

'''
''' 4.Program to find the square of the given number
n = int(input("Enter number "))
square = n * n
print(square)

'''
''' 5.Program to find the cube of the given number
n = int(input("Enter a number: "))
cube = n * n * n
print("Cube =", cube)

'''

'''6.Program to find the sum of square and cube of a given number
n = int(input("Enter  number "))
square = n * n
cube = n * n * n
result = square + cube
print(result)

'''
'''7.Program to display the last digit of a given number
n = int(input("Enter a number: "))
last_digit = n % 10
print(last_digit)

'''
'''8.Program to remove the last digit of a given number
n = int(input("Enter a number: "))
result = n // 10
print("Number after removing last digit =", result)

'''

'''9.Program to find the sum of first N numbers
n = int(input("Enter N value: "))
i = 1
sum= 0
while i <= n:
    sum += i
    i += 1
print(sum)

'''

'''10.Program to swap 2 numbers
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
temp = a
a = b
b = temp
print(a)
print(b)

'''
'''11.Program to swap 2 numbers without using 3rd variable
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
a = a + b
b = a - b
a = a - b
print(a)
print(b)

'''
'''12.Program to calculate the total amount for the given quantity of fruits purchased
quantity = int(input("Enter quantity of fruits: "))
price = float(input("Enter price of one fruit: "))
total = quantity * price
print(total)

'''
'''13.Program to find the total salary for the given basic salary
basic = float(input("Enter basic salary: "))
da = float(input("Enter DA: "))
hra = float(input("Enter HRA: "))
total_salary = basic + da + hra
print(total_salary)

'''
'''14.Program to calculate Area of Circle
r = float(input("Enter radius: "))
area = 3.14 * r * r
print(area)

'''
'''15.Program to calculate Area of Triangle
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print( area)

'''
'''16.Program to calculate Time Taken using Speed and Distance
distance = float(input("Enter distance: "))
speed = float(input("Enter speed: "))
time = distance / speed
print(time)

'''

'''17.Program to calculate Speed using Distance and Time
distance = float(input("Enter distance: "))
time = float(input("Enter time: "))
speed = distance / time
print(speed)

'''
'''18.Program to calculate Distance using Speed and Time
speed = float(input("Enter speed: "))
time = float(input("Enter time: "))
distance = speed * time
print(distance)

'''

'''19.Program to give 20% bonus on salary if employee has more than 5 years of experience
salary = float(input("Enter salary: "))
experience = int(input("Enter years of experience: "))
if experience > 5:
    bonus = 0.20 * salary
    salary = salary + bonus
print(salary)

'''

'''20.Give 10% discount on total purchase if the customer is a member and the bill amount is greater than 1000.
bill = float(input("Enter bill amount: "))
member = input("Are you a member? (yes/no): ")
if member == "yes" and bill > 1000:
    discount = 0.10 * bill
    bill = bill - discount
print("Pay:", bill)

'''

'''21.Program to give a 15% discount on hotel booking if the stay duration is more than 7 days.
bill = float(input("Enter hotel booking amount: "))
days = int(input("Enter stay duration: "))
if days > 7:
    discount = 0.15 * bill
    bill = bill - discount
print(bill)

'''
'''22.Give a 10% discount on grocery items if the total quantity purchased is more than 20.
bill = float(input("Enter total bill amount: "))
quantity = int(input("Enter total quantity: "))
if quantity > 20:
    discount = 0.10 * bill
    bill = bill - discount
print("Pay:", bill)

'''

'''23.Give a 5% bonus on salary if the employee's attendance is perfect for the month (no absences).
salary = float(input("Enter salary: "))
absences = int(input("Enter number of absences: "))
if absences == 0:
    bonus = 0.05 * salary
    salary = salary + bonus
print(salary)

'''

'''24.Program to give a 20% discount on gym membership if the customer signs up for a year.
bill = float(input("Enter gym membership amount: "))
duration = int(input("Enter membership duration in months: "))
if duration == 12:
    discount = 0.20 * bill
    bill = bill - discount
print(bill)

'''
'''25.Program to give ₹200 cashback and add it to the credit card amount if the user pays a minimum of 50% of the credit card bill amount. Display the final credit limit.
bill = float(input("Enter credit card bill amount: "))
paid = float(input("Enter amount paid: "))
credit_limit = float(input("Enter credit limit: "))
if paid >= 0.50 * bill:
    credit_limit = credit_limit + 200
    print("Cashback: 200")
else:
    print("Cashback: 0")
print(credit_limit)

'''
'''26.Program to print numbers 2, 4, 6, 8, 10
for i in range(2, 11, 2):
    print(i)
'''

'''27.Program to print numbers 15, 12, 9, 6, 3, 0
for i in range(15, -1, -3):
    print(i)

'''
'''28.Program to print numbers 10, 20, 30, 40, 50
for i in range(10, 51, 10):
    print(i)
'''

'''29.Program to print numbers 100, 80, 60, 40, 20
for i in range(100, 0, -20):
    print(i)
'''
'''30.Program to print lowercase alphabets a to z
for i in range(97, 123):
    print(chr(i), end=" ")
'''
'''31.Program to print uppercase alphabets in reverse order Z to A
for i in range(90, 64, -1):
    print(chr(i), end=" ")
'''
'''32.Program to print ASCII values from A to Z
for i in range(65, 91):
    print(i, "=", chr(i))

'''
'''33.Program to print ASCII values from a–z
for i in range(97, 123):
    print(i, "=", chr(i))
'''

'''34.Program to print ASCII values of 0–9
for i in range(48, 58):
    print(i, "=", chr(i))
'''

'''35.Program to display ASCII character set
for i in range(128):
    print(i, "=", chr(i))
'''

'''36.Program to print square values for numbers 1 to 5
for i in range(1, 6):
    print(i, "=", i * i)
'''

'''37.Program to print cube values for numbers 1 to 5
for i in range(1, 6):
    print(i, "=", i * i * i)
'''

'''38.Program to find the sum of first N numbers
n = int(input("Enter N value: "))
sum= 0
for i in range(1, n + 1):
    sum = sum+ i
print(Sum)

'''
'''39.Program to find factorial of a number
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(fact)

'''
'''40.Program to print numbers divisible by 7 between 20 and 60
for i in range(20, 61):
    if i % 7 == 0:
        print(i)
'''

'''41.Program to print numbers divisible by 3 and not divisible by 5 between 10 and 50
for i in range(10, 51):
    if i % 3 == 0 and i % 5 != 0:
        print(i)

'''

'''42.Program to print numbers divisible by 4 and not divisible by 100 from 100 to 300
for i in range(100, 301):
    if i % 4 == 0 and i % 100 != 0:
        print(i)
'''

'''43.Program to print numbers which are not divisible by 5 from 30 to 70
for i in range(30, 71):
    if i % 5 != 0:
        print(i)

'''
'''44.Program to print even numbers from 1 to 30 which are not divisible by 5
for i in range(1, 31):
    if i % 2 == 0 and i % 5 != 0:
        print(i)
'''
'''45.Program to display multiplication table
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

'''
'''46.Program to print even numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
'''
'''47.Program to find the sum of even numbers from 1 to 10
total = 0
for i in range(1, 11):
    if i % 2 == 0:
        total = total + i
print("Sum of even numbers =", total)

'''
'''48.Program to count factors of a given number
n = int(input("Enter a number: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1
print("Count of factors =", count)

'''

'''49.Program to print factors of a given number

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
'''

'''50.Program to count factors of a given number (using while loop)
n = int(input("Enter a number: "))
i = 1
count = 0

while i <= n:
    if n % i == 0:
        count += 1
    i += 1
print("Total factors =", count)

'''

'''51.Program to find the sum of factors of a given number
n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    if n % i == 0:
        total = total + i
print("Sum of factors =", total)

'''

'''52.Program to check whether the input number is Prime or Not
n = int(input("Enter a number: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1
if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")

'''

'''53.Program to check whether the input number is Perfect or Not
n = int(input("Enter a number: "))
total = 0
for i in range(1, n):
    if n % i == 0:
        total = total + i
if total == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

'''
'''54.Program to print Fibonacci Series
n = int(input("Enter number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
'''

'''55.Print multiplication table until user exits
while True:
    n = input("Enter a number (or q to exit): ")
    if n == 'q':
        break
    n = int(n)
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
'''

'''56.Check whether the number is Prime or Not until user exits
while True:
    n = input("Enter a number (or q to exit): ")
    if n == 'q':
        break
    n = int(n)
    count = 0
    if n > 1:
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
    if count == 2:
        print("Prime Number")
    else:
        print("Not a Prime Number")
'''
'''57.Program to display the last digit of a given number
n = 321875
last = n % 10
print("Last digit =", last)

'''

'''58.Program to remove the last digit of a given number
n = 321875
n = n // 10
print("After removing last digit =", n)

'''

'''59.Program to display all digits one by one in reverse order
n = 321875
while n > 0:
    digit = n % 10
    print(digit)
    n = n // 10

'''
'''60.Program to count the digits in a given number
n = 321875
count = 0
while n > 0:
    count = count + 1
    n = n // 10
print("Number of digits =", count)

'''
'''61.Program to find the sum of digits in a given number
n = 321875
total = 0
while n > 0:
    digit = n % 10
    total = total + digit
    n = n // 10
print("Sum of digits =", total)

'''
'''62.Program to check whether the last digit is even or not
n = 321875
last = n % 10
if last % 2 == 0:
    print("Last digit is Even")
else:
    print("Last digit is Odd")
    
'''
'''63.Program to display only even digits in the given number
n = 321875
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        print(digit)
    n = n // 10

'''

'''64.Program to find the sum of even digits in the given number
n = 321875
total = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        total = total + digit
    n = n // 10
print("Sum of even digits =", total)

'''
'''65.Program to count even digits in the given number

n = 321875
count = 0
while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        count = count + 1
    n = n // 10
print(count)

'''
'''66.Program to find the largest digit in the given number
n = 321875
largest = 0
while n > 0:
    digit = n % 10
    if digit > largest:
        largest = digit
    n = n // 1
print(largest)

'''

'''67.Program to find the smallest digit in the given number
n = 321875
smallest = 9
while n > 0:
    digit = n % 10
    if digit < smallest:
        smallest = digit
    n = n // 10
print(smallest)

'''

'''68.Program to check whether the number contains zero or not
n = 321875
found = False
while n > 0:
    digit = n % 10
    if digit == 0:
        found = True
        break
    n = n // 10
if found:
    print("Number contains zero")
else:
    print("Number does not contain zero")

'''
'''69.Program to find the average of all digits in the given number
n = 321875
total = 0
count = 0
while n > 0:
    digit = n % 10
    total = total + digit
    count = count + 1
    n = n // 10
average = total / count
print(average)

'''
'''
70.Program to find the second largest digit in the given number
n = 321875
largest = -1
second = -1
while n > 0:
    digit = n % 10
    if digit > largest:
        second = largest
        largest = digit
    elif digit != largest and digit > second:
        second = digit
    n = n // 10
print(second)

'''
'''71.Program to find the second smallest digit in the given number
n = 321875
smallest = 10
second = 10
while n > 0:
    digit = n % 10
    if digit < smallest:
        second = smallest
        smallest = digit
    elif digit != smallest and digit < second:
        second = digit
    n = n // 10
print("Second smallest digit =", second)

'''

'''72.Program to find the first digit in the given number
n = 321875
while n >= 10:
    n = n // 10
print("First digit =", n)

'''
'''73.Program to find the sum of first and last digits in the given number
n = 321875
last = n % 10
while n >= 10:
    n = n // 10
first = n
total = first + last
print("Sum of first and last digits =", total)

'''
'''74.Program to display multiplication table for each digit in the given number
n = 321875
for digit in str(n):
    digit = int(digit)
    print("Table of", digit)
    for i in range(1, 11):
        print(digit, "x", i, "=", digit * i)
    print()

'''

n=int(input("Enter the number"))
if n>0:
    print("positive number")