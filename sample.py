# Python3 program to add two numbers

number1 = input("First number: ")
number2 = input("\nSecond number: ")

# Adding two numbers
# User might also enter float numbers
sum = float(number1) + float(number2)

# Display the sum
# will print value in float
print("The sum of {0} and {1} is {2}" .format(number1, number2, sum))


def add(a,b):
  return a+b

num1 = 10
num2 = 5

sum_of_twonumbers = add(num1,num2)

print("Sum of {0} and {1} is {2};" .format(num1,num2, sum_of_twonumbers))