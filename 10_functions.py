# A function is a block of code which only runs when it is called. 
# You can pass data, known as parameters, into a function. 
# A function can return data as a result
# In python functions are defined using the def keyword

# LETS CALL A FUNCTION
# def greet_user():
#     print("Hello.User!")

# greet_user()

# def aoa():
#     print("Hi")

# aoa()

# def aoa(name):
#     print(f"Hi {name}!, Kaifa Haluk")

# aoa("Usama")
# def aoa(name = "Ali"):
#     print(f"Hi {name}!, Kaifa Haluk")

# aoa("Azam")


# Return Values

# def square(number):
#     return number * number
# print(square(9))

                          ### Recursion
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))

                   ### Lambda functions
# x = lambda a : a + 10
# print(x(5))
# x = lambda a : a / 10
# print(x(5))

# x = lambda a, b : a * b 
# print(x(5, 10))

def x(a,b):
    return a * b
print(x(5, 10))