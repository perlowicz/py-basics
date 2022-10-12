from re import X


# str = input("Enter your name: ")
# print(type(str))

# #------------
# variables
# x = 10.2
# y = 99
# # print(y/x) -> error
# print(str(y/x))
# print(type(y/x))

# #--------------

# age = float(input("Enter your age:"))
# print(type(age))

# #---------------
# strings
# course = 'python for beginners'
# print(course.capitalize())
# print(course.replace("n","$"))
# print(type('python' in course))

#---------------------
# arithmetic operators
a = 5
print(10 + 3)
print(10 // 3)
print(10 * 3)
print(10 % 3)
print(2 ** 3)
a+=a
print("a -> " + str(a))

#comparsion

val = 3 == 2
print(val)
#reszta jak w javie

#logical operators
price = 25
print(price < 100 and price == 25)
print(price > 0 or not price < 0)

#if statement
temp = 35
if temp > 30 : 
    print("Hot!")
else :
    print("Cold!")

if 10 > 2:
    print("Test1")
    print("Test2")
#w pythonie nie występują klamry! widoczność kodu określa się formatowaniem tekstu

# while loop
