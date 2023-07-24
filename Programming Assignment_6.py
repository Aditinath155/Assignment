#!/usr/bin/env python
# coding: utf-8

# # Programming Basic Assignment 6

# ### 1. Write a Python Program to Display Fibonacci Sequence Using Recursion?

# ### 2. Write a Python Program to Find Factorial of Number Using Recursion?

# ### 3. Write a Python Program to calculate your Body Mass Index?

# ### 4. Write a Python Program to calculate the natural logarithm of any number?

# 
# ### 5. Write a Python Program for cube sum of first n natural numbers?
# 

# In[1]:


#1. Write a Python Program to Display Fibonacci Sequence Using Recursion?
#Fibonacci series is a sequence of each number is the sum of the two preceding ones.
#Recursion is a programming technique where a function calls itself
#It breaks down the original problem into simpler sub-problems, and the function keeps calling itself until it reaches a base case, where the recursion stops.

#Define the function 

def fibo(n):
    if n <= 1:
        return n 
    else:
        return fibo(n-1) + fibo(n-2)
    
#Take user input

n = int(input('Enter positive number: '))

#Condition
if n <= 0:
    print("******Enter correct number*****")
else:
    print('Factorial number')
    for i in range(n):
        print(fibo(i))


# In[1]:


# 2. Write a Python Program to Find Factorial of Number Using Recursion?
#Logic = n*(n-1)
#E.g 5! = 5*4*3*2*1

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1) #ek tarike se loop change kar rha 

n = int(input('Enter positive number: '))
#Condition
if n <= 1:
    print("******Enter correct number*****")
else:
    print('Factorial number')
    print(fact(n))


# In[2]:


# 3. Write a Python Program to calculate your Body Mass Index?
# It is calculated by dividing the weight of a person (in kilograms) by the square of their height (in meters). 
#BMI= Weight/height**height

#Define the function 
def BMI(weight,height):
    #give 2 parameter according to the formula
    cal_bmi = weight/(height*height)
    return cal_bmi
#Take user input
weight_kg = float(input('Enter your weightin kg : '))
height_m = float(input('Enter your height in meter : '))

#Calculate BMI
Calculate_BMI = BMI(weight_kg,height_m)

print('Your BMI is: ',Calculate_BMI)


# In[3]:


# 4. Write a Python Program to calculate the natural logarithm of any number?
#import math function
import math

# Take user input for the number
num = float(input("Enter a positive number to calculate its natural logarithm: "))

if num <= 0:
    print("Please enter a positive number.")
else:
    # Calculate the natural logarithm
    result = math.log(num)

  
    print("The natural logarithm of", num, "is:", result)


# In[4]:


# 5. Write a Python Program for cube sum of first n natural numbers?
#Take input from user
n = int(input('Enter a positive integer: '))
result = 0
if n <= 1:
        print("Please enter a positive integer.")
else:
    for i in range(1,n+1):
            result = result + pow(i,3)

#Print the result
    print("Cube sum of first n natural number",result)


# In[ ]:




