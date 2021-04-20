# if statement
"""
Syntax
    if(condition):
        statement for true

# Condition
    value relational_operator value
    # ==, !=, >, <, >=, <=
    # result -> True or False

# Example
num1 = 1 # initialize / store
if(num1 == 0): # compare equals to ; value of num1 is equals to zero
    print("ZERO")
print("END")


# if else
Syntax
    if (Condition):
        Statement for True
    else:
        Statement for False

# Example
num1 = 0
if(num1==0):
    print("ZERO")
else:
    print("OTHERS")


# if ... elif statement
# Syntax
if (condition1):
    Statement for true
elif (Condition2):
    Statement for true
elif (Condition3):
    Statement for true
else:
    Statement for false
"""
#Example
num1 =5
if (num1 == 0):
    print("ZERO")
elif (num1==1):
    print("ONE")
elif(num1==2):
    print("TWO")
else:
    print("OTHER")

# nested if
"""
if (condition1):
    if(condition2):
        Statement for true
"""
# Example
num1=9
num2=8
num3=4
if(num1>num2):
    if(num1>num3):
        print(num1)

# if statement with logical operator
"""
if(condition1 logical_operator condition2)
    Statement for true
Note:
- and, or
"""
num1 = 8
num2 = 5
num3 = 2

if((num1>num2) and (num1>num3)):
    print(num1)

# 2. Looping statements
"""
print("Broadway")
print("Broadway")
print("Broadway")
print("Broadway")
print("Broadway")
"""
count = 1
while(count<=5):
    print("Broadway Infosys")
    count+=1

# Tasks
"""
    1. print 1 to 10
    2. print first no to last no
    3. print sum of 1 to 10
    4. print average of 1 to 10
    5. print factorial of 1 to 10
    6. print odd numbers between 1 to 10
    7. print even numbers between 1 to 10
    8. print sum of odd numbers between 1 to 10
    9. print sum of even numbers between 1 to 10
"""
# for loop
for i in range(5): # 0 to 4
    print(i)
print()
for i in range(1, 6): # 1 to 5
    print(i)
print()
for i in range(1, 21, 2): # 1, 3, 5, 7, ....<21
    print(i)
print()

# nested loop
for i in range (5): # 0 to 4
    for j in range(5): # 0 to 4
        print(i * j)
    print()
print()


# break and continue
print("-----------------")
for i in range(10):
    if i == 5:
        break
    print(i)
print("-----------------")

# Continue statement
print("-----------------------")
for i in range(10):
    if i==5:
        continue
    else:
        print(i)
print("-----------------------")

# pass
class c1:
    pass

# return
def f1():
    return "Hello"

# range()
print(range(10))
var1 = range(10)
print(var1)