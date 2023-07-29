# Today = input("Please enter the name of the day: ")
# Time = int(input("Please enter the time: "))

# if Today  == 'Tuesday':
#     print("Nilkhet is closed today.")
# else:
#     if Time <= 19:
#         print("Nilkhet is open today. I can reach in time.")


# saarc = ["Bangladesh", "Afganistan", "Bhutan", "Nepal", "India", "Pakistan", "Sri Lanka"]
# country = input("Enter country name : ")
# if country in saarc:
#     print(country, "is a member of SAARC.")
# else:
#     print(country, "is not a member of SAARC.")
    
# print("Program Terminated.")

# marks = int(input("Please enter your marks:"))

# if marks >= 80:
#     grade = "A+"
# elif marks >= 70:
#     grade = "A"
# elif marks >= 60:
#     grade = "A-"
# elif marks >= 50:
#     grade = "B"
# elif marks >= 40:
#     grade = "C"
# else:
#     grade = "F"

# print("Your grade is: ", grade)


# num = int(input("Please enter a number: "))

# if num % 2 == 0:
#     print(num, "is even.")
# else:
#     print(num, "is odd.")


# n1 = int(input("Please enter a number: "))
# n2 = int(input("Please enter another number: "))
# n3 = int(input("Please enter another number: "))

# if n1 > n2 and n1 > n3:
#     print(n1, "is the largest number.")
# elif n2 > n1 and n2 > n3:
#     print(n2, "is the largest number.")
# else:
#     print(n3, "is the largest number.")

# if n1 > n2:
#     max_n = n1
# else:
#     max_n = n2
# if n3 > max_n:
#     max_n = n3

# print("Maximum:", max_n)


# year = int(input("Please enter a year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(year, "is a leap year")
#         else:
#             print(year, "is not a leap year")
#     else:
#         print(year, "is a leap year")    
# else:
#     print(year, "is not a leap year")


# year = int(input("Please enter a year:"))

# if year % 100 != 0 and year % 4 == 0:
#     print(year,"is a leap year")
# elif year % 100 == 0 and year % 400 ==0:
#     print(year,"is a leap year")
# else:
#     print(year,"is not a leap year")


# for i in range(5):
#     print(i)


# import turtle
# turtle.shape("turtle")
# turtle.speed(1)

# for i in range(4):
#     turtle.forward(100)
#     turtle.left(90)

# turtle.exitonclick()


# result = 0
# for i in range(50):
#     result += 1 # result = result + 1
#     print(result)

# print('  ', result)


# result = 0
# num = 1

# for _ in range(4):
#     result = result + num
#     num = num + 1

# print(result)


# result = 0
# for num in range(51):
#     result = result + num
# print(result)


# result = 0
# for num in range(1,51):
#     result += num
# print(result)


# for i in range(1, 20, 5):
#     print(i)


# numbers = [5555,332,357,6574,1243,6532,0]
# max_n = numbers[0]
# for n in numbers:
#     if n > max_n:
#         max_n = n
# print(max_n)


# result = 0
# for num in range(101):
#     if num % 5 == 0:
#         print(num)
#         result += num
# print("Sum is:",result)


# import turtle

# turtle.speed(1)

# for i in range(20):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(3)
#     turtle.pendown()

# turtle.exitonclick()


# import turtle
# turtle.shape("turtle")
# turtle.speed(1)

# for side_length in range(50, 100, 10):
#     for i in range(4):
#         turtle.forward(side_length)
#         turtle.left(90)

# turtle.exitonclick()


# saarc = ["Bangladesh", "Afganistan", "Bhutan", "Nepal", "India", "Pakistan", "Sri Lanka"]
# for country in saarc:
#     print(country, "is a member of SAARC")


# li = list(range(11))
# print(li)

# li = list(range(2,21,2))
# print(li)


# i = 0
# while i < 5:
#     print(i)
#     i += 1


# i = 5
# while i >= 0:
#     i -= 1
#     print(i)


# n = int(input("Please enter a positive integer: "))

# m = 0
# while m <= 10:
#     print(f"{n} x {m} = {n*m}")
#     m += 1


# import turtle
# turtle.color("blue")
# turtle.speed(5)

# counter = 0
# while counter < 36:
#     for i in range(4):
#         turtle.forward(100)
#         turtle.right(90)
#     turtle.right(10)
#     counter += 1
    
# turtle.exitonclick()


# import turtle

# height = int(input())

# width = int(input())

# turtle.speed(2)

# turtle.penup()

# for y in range(height):
#     for x in range(width):
#         turtle.dot()
#         turtle.forward(20)
#     turtle.backward(20 * width)
#     turtle.right(90)
#     turtle.forward(20)
#     turtle.left(90)

# turtle.exitonclick()


# while True:
#     n = int(input("Please enter a number (0 to exit): "))
#     if n == 0:
#         print("The program closed.")
#         break
#     print("Square of", n, "is", n*n)



# while True:
#     n = int(input("Please enter a number (0 to exit): "))

#     if n < 0:
#         print("Only positive numbers are allowed. Please try again.")
#         continue

#     if n == 0:
#         print("The program closed.")
#         break
#     print("Square of", n, "is", n*n)


# terminate = False
# while not terminate:
#     num1 = int(input("Please enter a number: "))
#     num2 = int(input("Please enter another number: "))

#     while True:
#         operation = input("Please enter add/sub or quit to exit: ")
#         if operation == "quit":
#             terminate = True
#             print("The program closed successfully.")
#             break
#         if operation not in ["add", "sub"]:
#             print("Unknown operation!")
#             continue
#         if operation == "add":
#             print("Result is: ", num1 + num2)
#             break
#         if operation == "sub":
#             print("Result is: ", num1 - num2)
#             break


# def add(n1, n2):
#     return n1 + n2

# n = int(input())
# m = int(input())
# result = int(add(n,m))
# print(result)

# import turtle

# turtle.speed(100)

# def draw_sqr(side_length):
#     for i in range(4):
#         turtle.forward(side_length)
#         turtle.left(90)

# counter = 0
# while counter < 90:
#     draw_sqr(100)
#     turtle.right(4)
#     counter += 1
# turtle.exitonclick()


# def myfnc(x):
#     print("inside myfnc", x)
#     x = 10
#     print("inside myfnc", x)

# x = 20
# myfnc(x)
# print(x)


# def myfnc(y):
#     print("y =", y)
#     print("x =", x)

# x = 20
# myfnc(x)
# print("y =", y)


# def myfnc(y=10):
#     print("y =", y)

# x = 20
# myfnc(x)
# myfnc()


# def myfnc(x, y = 10, z):
#     print("x =", x, "y =", y, "z =", z)

# x = 5
# y = 6
# z = 7
# myfnc(x, y, z)



# def myfnc(x, y = 10, z=0):
#     print("x =", x, "y =", y, "z =", z)

# x = 5
# y = 6
# z = 7
# myfnc(x, y, z)
# myfnc(x, y)
# myfnc(x)


# def myfnc(x, z, y = 10):
#     print("x =", x, "y =", y, "z =", z)

# myfnc(x= 1, y = 2, z = 5)
# a = 5
# b = 6
# myfnc(x = a, z = b)
# a = 1
# b = 2
# c = 3
# myfnc(y = a, z = b, x = c)


# def add_numbers(numbers):
#     result = 0
#     for number in numbers:
#         result += number
#     return result

# result = add_numbers([1, 2, 3, 4, 5, 9])
# print(result)


# def test_fnc(li):
#     li[0] = 10

# my_list = [1, 2, 3, 4]
# print("before function call", my_list)
# test_fnc(my_list)
# print("after function call", my_list)


# list1 = [1, 2, 3, 4]
# list2 = list1

# print(list1)
# print(list2)
# list2[0] = 100
# print(list2)
# print(list1)

# li3 = [1, 2, 3, 4, 5, 6, 7, 8]
# result = sum(li3)
# print(result)


# def greet():
#     print("Good day!")
# greet()
# print("Thank you")



# def greet(name, time):
#     print(f"Good {time}, {name}")

# # greet("Tousif", "Night")
# # greet("Tousif", "Morning")
# # greet("Abid")


# greet(time= "Evening", name = "Tousif")
# greet("Tousif", time="Night")  right//
# greet(time="Night", "Tousif")  wrong//
# greet("Morning", name="Tousif") wrong//


# def greet(*names):
#     for x in names:
#         print(f"Hello, {x}")

# greet("Jack", "James", "John", "Sherly", "Tousif", "Abid")



# def name(**names):
#     print("First Name: ", names['fname'])
#     print("Last Name: ", names['lname'])

# name(fname = "Tousif", lname = "Haq")



# def greet_1(name = "Buddy", time = "Morning"):
#     print(f"Good {time}, {name}")

# greet_1(name = "Tousif", time = "Evening")
# greet_1(name = "Tousif")
# greet_1()
# greet_1(time = "Night")



# def func(apn):
#     apn.append(6)
#     print(apn)

# list_1 = [1,2,3,4,5]
# print(list_1)
# func(list_1)
# print(list_1)   mutable



# def func(s):
#     s = s.replace("H", "J")
#     print(s)

# string = "Hello"
# print(string)
# func(string)
# print(string)   immutable 



# def peri_rect(h, w):
#     peri = 2*(h + w)
#     return peri

# p = peri_rect(6,2)
# print("The perimeter is: ", p)



