# If else conditional statements
a = int(input("Enter your age:"))
print("Your age is:", a)
# If a is 14
print(a>18) #False
print(a>=18) #False
print(a<=18) #True
print(a<18) #True
if(a >= 18):
  print("You can drive")
else:
  print("You cannot drive") # This gets executed

# Example1
Appleprice = 10
Budget = 200
if(Budget - Appleprice == 50):
  print("Alexa, add 1 kg Apples to the cart.")
elif(Budget - Appleprice > 70):
  print("It's okay you can buy")
else:
  print("Alexa, do not add Apples to the cart.")

# Example2
num = int(input("Enter the value of num:"))
if(num < 0):
  print("Number is Negative")
elif(num == 0):
  print("Number is Zero")
else:
  print("Number is Positive")

# Example3
num = 18
if(num < 0):
  print("Number is Negative")
elif(num > 0):
  if(num <= 10):
    print("Number is between 1-10")
  elif(num > 10 and num <= 20):
    print("Number is between 11-20")
  else:
    print("Number is greater than 20")
else:
  print("Number is Zero")
