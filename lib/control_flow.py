#!/usr/bin/env python3

def admin_login(username, password):
    saved_name = username.upper()
    if saved_name == 'ADMIN' and password == str(12345):
        print('Access Granted')
    else:
        print('Access Denied')


def hows_the_weather(temperature):
   if temperature < 40 :
       print("It's brisk out there!")
   elif temperature > 40 and temperature < 65 :
        print("It's a little chilly out there!")
   elif temperature > 85 : 
       print("It's too dang hot out there!")
   else:
        print("It's perfect out there!")

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '/':
        return num1 / num2
    elif operation == '*':
        return num1 * num2
    else:
        print( "Invalid operation!" )
        return None



calculator("+", 1, 1)