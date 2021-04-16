from my_libs import MyFunctions # import Python File
"""
for i in range(10):
    MyFunctions.f1()  # Call the function
"""
# single line comment
"""
multi-line comments
"""
"""
var1 ="Broadway InfoSys"
# passing value to function
MyFunctions.f2(var1) # Argument # Passing value to function



# f2(num1, num2) # function signature - function name and list of paramter(s)

num1 = 9
num2 = 8
MyFunctions.f2(num1, num2)

num1 = 90
num2 = 18
MyFunctions.f2(num1, num2)

num1 = int(input("Enter first no : "))
num2 = int(input("Enter second no : "))
MyFunctions.f2(num1, num2)
"""

num1 = MyFunctions.f3()
print(num1)
