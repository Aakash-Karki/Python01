from oops.MyClasses import *

obj1 = Class1() # Object declare and initialize
print(obj1)
print(type(obj1))
print(id(obj1))
print(isinstance(obj1, Class1))

obj2 = Class2()
obj3 = Class2()

print(obj2)
print(type(obj2))
print(id(obj2))
print(isinstance(obj2, Class1))
print(isinstance(obj2, Class2))

# Accessing class variable
print(obj2.id)
print(obj2.name)
print(obj2.address)
print()

print(obj3.id)
print(obj3.name)
print(obj3.address)
print()

# Update value
obj2.id = 2
obj2.name="Raj Thapa"
obj2.address="BHK, Nepal"

print(obj2.id)
print(obj2.name)
print(obj2.address)

obj3 = obj2

obj3 = Class2()
print("______________________________")
# Accessing instance variable
obj4 = Class4()
print(obj4.id, obj4.name, obj4.address)
print(obj4)
print("______________________________")
# Updating values
obj4.id=2
obj4.name="New Name"
obj4.address="Bhaktapur, Nepal"
print(obj4.id, obj4.name, obj4.address)
print(obj4)# call __str__() method
print("______________________________")
obj5 = Class5(1, "Your name", "Your address")
print(obj5)
print("______________________________")
obj6 = Class6(1)
print(obj6.getId())
print(obj6)
obj6.setId(2)
print(obj6.getId())
print(obj6)
print("-------------------------------------")
obj7 = Class7(2)# Class7() -> __init__(self, id=-1)
print(obj7)
obj7_1 = Class7()# Class7() -> __init__(self, id=-1)
print(obj7_1)
print("-------------------------------------")
obj8 = Class8(1, "Raj")# Object declare and initialize
#print(obj8.id) #AttributeError: 'Class8' object has no attribute 'id'
print(obj8.getID(), obj8.getFullName())
print(obj8)
print("-------------------------------------")