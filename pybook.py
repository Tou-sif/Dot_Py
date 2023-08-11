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



# s = 'Dimik\'s'
# print(s)



# c = ['A','B','C']
# for value, index in enumerate(c):
#     print(index, value)

# v = list(enumerate(c))
# for i in v:
#     print(i)

# print(v)
    


# desh = "Bangla" + "desh"
# print(desh)

# x = 50 + 5
# print(x)

# y = "50" + "5"
# print(y)



# country = "Bangladesh"
# print(country.find("Bengla"))   # if the selected string is not found it returns -1.



# country = "North Korea"
# print(country)
# new_country = country.replace("North", "South")
# print(new_country)


# text = "this is a test. this is another test. this is the final test."
# text = text.replace("this", "This")
# print(text)



# n_txt = " this is a test string with spaces. "
# for i in range(6):
#     print(n_txt)
#     print(n_txt.lstrip())
#     print(n_txt.rstrip())
#     print(n_txt.strip())
#     print(n_txt)



# c1 = "bangladesh"


# c1_up = c1.upper()
# print(c1_up.upper())

# c1_low = c1.lower()
# print(c1_low)

# c1_cap = c1.capitalize()
# print(c1_cap)


# wish = "I want to be free of worries"

# # wish_split = wish.split()
# # for i in  wish_split:
# #     print(i)

# # print(wish_split)
# # print(wish)


# print(wish.count("e"))
# print(wish.startswith("i"))
# print(wish.endswith("es"))



# name = "Mr Anderson"
# if name.startswith("Mr"):
#     print("Dear Sir")



# import turtle

# name = turtle.textinput("Name", "What is your name?")
# name = name.lower()
# if name.startswith("mr"):
#     print("Hello Sir, how are you?")
# elif name.startswith("mrs") or name.startswith("miss") or name.startswith("ms"):
#     print("Hello Madam, how are you?")
# else:
#     name = name.capitalize()
#     str = (f"Hi, {name} How are you?")
#     print(str)

# turtle.exitonclick



# str = "a quick brown fox jumps over the lazy dog"
# for c in "abcdefghijklmnopqrstuvwxyz":
#     print(c, str.count(c))



# str = input("Please enter a word: ")
# rts = str [::-1]

# if str == rts:
#     print(str, "is a palindrome")
# else:
#     print(str, "is not a palindrome")




# str = input()
# ans = ""
# for position in range(0,len(str),2):
#     ans += str[position^1] + str[position]

# print(ans)



# str = input()
# ans = ""

# for pos in range(0,len(str)):
#     ans += str[pos^1]
# print(ans)



# def filter_letters(input_string):
#     uppercase_letters = []
#     lowercase_letters = []
#     digits = []
#     symbols = []

#     for char in input_string:
#         if char.isupper():
#             uppercase_letters.append(char)
#         elif char.islower():
#             lowercase_letters.append(char)
#         elif char.isdigit():
#             digits.append(char)
#         else:
#             symbols.append(char)


#     return uppercase_letters, lowercase_letters, digits, symbols


# input_string = input()
# uppercase_letters, lowercase_letters, digits, symbols = filter_letters(input_string)

# print("Uppercase letters:", "".join(uppercase_letters))
# print("Lowercase letters:", "".join(lowercase_letters))
# print("Digits:", "".join(digits))
# print("symbols:", "".join(symbols))



# Target hours of employees.
# hours = eval(input())  #[int(hours) for hours in input().split()] This is the main comment
# target = int(input())

# app_values = [num for num in hours if num >= target]
# if app_values:
#     count_app_values = len(app_values)
#     print(count_app_values)
# else:
#     print(len(app_values))



# li = [1,3,45,7,9,0,11]

# li_sort = li.sort()

# print(li)


# list_a = ['apple', 'orange', 'banana', 'sugarcane', 'pineapple']
# print(list_a)
# item = int(input())
# if item in list_a:
#     list_a.remove(item)
#     print(list_a)
# else:
#     print(item, "not in list")



# list_a = ['apple', 'orange', 'banana', 'sugarcane', 'pineapple']
# print(list_a)
# for index, val in enumerate(list_a):
#     print(index + 1, val)

# item = list_a.pop(int(input())-int(1))
# print(item)
# print(list_a)



# li_1 = [1,2,3]
# lii_2 = [3,4,5,6,7]

# li_1.extend(lii_2)
# print(li_1)
# print(li_1.count(10))



# fruits = ['apple', 'orange', 'mango', 'banana', 'guava']
# item = fruits.pop(2)
# print(f"You poped a {item}")
# print(fruits)



# blank_list = []
# for _ in range(1,4):
#     blank_list.append(_)
# print(blank_list)
# lis_0 = [4,5,6]
# print(blank_list + lis_0)
# print(blank_list * 3)



# li = ['a', 'b', 'c', 'd']
# print(li)
# str = "-".join(li)
# print(str)



# list_a = [1,2,3,4]
# list_2a = []

# for x in list_a:
#     list_2a.append(2*x)

# print(list_2a)
# _1 =  "-".join(map(str,list_2a))
# print(_1)



# li = [1,2,3,4]
# new_li = []
# for x in li:
#     new_li.append(2 *x)

# print(new_li)

# nw_li = [2 * x for x in li if 2*x % 2 == 0]
# print(nw_li)



# all_nums = [1,2,3,4,5,6,7,8,9,10]
# # even_nums = []
# # odd_nums = []
# # for x in all_nums:
# #     if x %2 == 0:
# #         even_nums.append(x)
# #     else:
# #         odd_nums.append(x)

# # print(even_nums)
# # print(odd_nums)

# even_nums = [x for x in all_nums if x %2 == 0]
# print(even_nums)
# odd_nums = [x for x in all_nums if x %2 != 0]
# print(odd_nums)



# list_of_nums = [1,2,3,4,5]
# sqr_of_nums = [x ** 2  for x in list_of_nums]
# print(sqr_of_nums)



# x = (1,2,3,4,5)
# print(x)
# x[0] = 6 # for observation purposes the tuple doesn't support item assignment
# y = [1,2,3,4,5]
# print(y)

# y[0] = 10
# print(y)
# # this code will not run



# numbers = (10,20,30,40)
# n1, n2, n3, n4 = numbers
# n34 = n3, n4
# print(n1, n2, n3, n4, n34)



# items_tup = (1,2,5.5, 'Tou', ['a', 'b', 'c'], ('apple', 'mango'))
# for item in items_tup:
#     print(item, type(item))

# tups_list = list(items_tup)
# print(type(tups_list))
# for index, value in enumerate(tups_list):
#     print(f"Sl:{index + 1}-", value, type(value))


# b, w, y = 6,8,7
# total = b + w + y
# prob_bw = (b / total) * (w / (total-1))
# print(prob_bw)   #problem by saiham, drawing balck ball and then white ball consecutively



# items_set = {'pen', 'ball', 'laptop'}
# print(items_set, type(items_set))

# li = [1,2,3,4]
# tpl = (1,2,3,)
# A = set(li)
# B = set(tpl)
# print(A)
# print(B)

# country = set("Bangladesh")
# print(country)
# country_2 = set("Sri Lanka")
# print(country_2)
# print("S" in country)

# new_country = country & country_2
# print(new_country)
# new_country2 = country | country_2
# print(new_country2)
# new_country3 = country ^ country_2
# new_country4 = country - country_2
# print(new_country3)
# print(new_country4)



# marks = [77,78,91,86,74,80,98,99,100,65,73]
# roll = int(input("Please enter your roll number: "))

# print("Marks:", marks[roll - 1])


# marks_2 = [[77,78],[91,86],[74,80],[98,99],[100,65],[73,80]]
# roll_2 = int(input("Give roll number: "))
# print("Your marks:", marks_2[roll_2 - 1])



# marks = {1005: 77, 1002: 76, 1002: 62, 1004: 78, 1003: 65}
# print(marks[1003], type(marks))

# dt = {}
# print(type(dt))
# dt[1] = "one"
# dt[2] = "two"
# dt[3] = "three"
# print(dt[3])



# dt = {'a': 'A','b': 'B', 'c': 'C'}
# dt[(1,2,3)] = "tuple"
# print(dt)

# li = [1,2,3]
# dt[li] = "list"
# print(dt)



# marks = {"DH1001": {"Bangla": 74, "English": 89},"DH1002": {"Bangla": 70, "English": 75}}
# print(marks["DH1001"])
# marks["DH1003"] = {"Bangla": 68, "English": 72}
# print(marks)
# print(marks["DH1003"]["Bangla"])



# bd_division_info = {}
# bd_division_info["Barisal"] = {"district": 6, "upazila": 39, "union": 333}
# bd_division_info["Chittagong"] = {"district": 11, "upazila": 97, "union": 336}
# bd_division_info["Dhaka"] = {"district": 13, "upazila": 93, "union": 1833}
# bd_division_info["Khulna"] = {"district": 10, "upazila": 59, "union": 270}
# bd_division_info["Mymensingh"] = {"district": 4, "upazila": 34, "union": 350}
# bd_division_info["Rajshahi"] = {"district": 8, "upazila": 70, "union": 558}
# bd_division_info["Rangpur"] = {"district": 8, "upazila": 58, "union": 536}
# bd_division_info["Sylhet"] = {"district": 4, "upazila": 38, "union": 334}

# divisions = bd_division_info
# for key in bd_division_info:
#     print(key)
#     print(bd_division_info[key])

# for key, value in bd_division_info.items():
#     print(key)
#     print(value)



# import random

# print(random.random())
# print(random.randint(10,50))



# import turtle
# import random
# turtle.penup()
# for i in range(20):
#     x = random.randint(-200, 200)
#     y = random.randint(-200, 200)
#     turtle.setposition(x,y)
#     turtle.dot()

# turtle.exitonclick()



# import turtle
# import random

# colors = ['red', 'green', 'blue', 'yellow','orange', 'black', 'purple']
# turtle.penup()

# for i in range(50):
#     x = random.randint(-100, 100)
#     y = random.randint(-100, 100)

#     turtle.setposition(x,y) # set a random position
#     random_color_index = random.randint(0, len(colors) - 1) # set a random color
#     select_color = colors[random_color_index]
#     turtle.dot(select_color)

# turtle.exitonclick()



# import random
# number = random.randint(1, 1000)
# attempts = 0

# while True:
#     input_number = int(input("Guess the number between 1 and 1000: "))
#     attempts += 1
#     score = 1000
#     if input_number == number:
#         print("Correct!")
#         break
#     if input_number > number:
#         print("Too big! Try again.")
#     else:
#         print("Too small! Try again")

# print(f"You tried {attempts} times to find the correct number. Your score is {score - attempts}.")



# import random

# number = random.randint(1, 1000)
# attempts = 0
# score = 20
# low = 1
# high = 1000

# while True:
#     print("Guess the number between 1 and 1000: ")
#     input_number = (low + high) // 2 # only integer numbers because of integer division
#     print(f"My guess is: {input_number}")
#     attempts += 1

#     if input_number == number:
#         print("Correct!")
#         break
#     if input_number > number:
#         print("Too big! Try again.")
#         high = input_number - 1
#     else:
#         print("Too small! Try again")
#         low = input_number + 1

# print(f"You tried {attempts} times to find the correct number. Your score is {score - attempts}.")




# def is_prime(n):
#     if n < 2:
#         return False
#     prime = True
#     for x in range(2, n):
#         if n % x == 0:
#             print(f"{n} is divisiible by {x}")
#             prime = False
#             return prime # first change to optimize code
#     return prime

# while True:
#     number = int(input("Please enter a number (enter 0 to exit): "))
#     if number == 0:
#         break
#     prime = is_prime(number)
#     if prime is True:
#         print(f"{number} is a prime number.")
#     else:
#         print(f"{number} is not a prime number.")



# def is_prime_eff(n=1013):
#     if n == 2:
#         return True # 2 is a prime number
#     if n % 2 == 0:
#         print(f"{n} is divisible by 2.")
#         return False # all even numbers except 2 are non-prime numbers
#     if n < 2:
#         return False # numbers less than 2 are non-prime
#     prime = True
#     for x in range(3, n, 2):
#         if n % x == 0:
#             print(f"{n} is divisible by {x}.")
#             prime = False
#             return prime
#     return prime

# # while True:
# #     number = int(input("Please enter a number (enter 0 to exit): "))
# #     if number == 0:
# #         break
# #     prime = is_prime_eff(number)
# #     if prime is True:
# #         print(f"{number} is a prime number.")
# #     else:
# #         print(f"{number} is not a prime number.")






# import math

# def is_prime_final(n=1013):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     m = math.sqrt(n)
#     m = int(m) + 1
#     for x in range(3, m, 2):
#         if n % x == 0:
#             return False
#     return True

# import timeit
# t1 = timeit.timeit(is_prime_eff)
# t2 = timeit.timeit(is_prime_final)

# print(t1, t2, t1/t2)




# import turtle
# turtle.color('red', 'yellow')
# turtle.begin_fill()
# while True:
#     turtle.forward(200)
#     turtle.left(170)
#     if abs(turtle.position()) < 1:
#         break
# turtle.end_fill()
# turtle.exitonclick()


# import turtle
# turtle.begin_fill()
# turtle.forward(200)
# turtle.left(120)
# turtle.forward(200)
# turtle.left(120)
# turtle.forward(200)
# turtle.end_fill()

# turtle.exitonclick()




# fib_x = 1
# fib_next = 1
# n = int(input())

# if n <= 2:
#     fib_n = 1
# else:
#     i = 3
#     while i <= n:
#         i += 1
#         fib_temp = fib_x + fib_next
#         fib_x = fib_next
#         fib_next = fib_temp

#     fib_n = fib_next

# print(fib_n)
