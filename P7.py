#String slicing and operations on string
name = "Replit,Program"
print(name[0:6])  # n to n-1 ; 0 to 5 ; Replit
print(len(name))  # 14
name1 = "Mango"
len1 = len(name1)
print("Mango is a", len1, "letter word")
# Mango is a 5 letter word
fruit = "Apple"
print(fruit[0:5]) # Apple
print(fruit[:5]) # Apple
print(fruit[:]) # Apple
print(fruit[1:5]) # pple
# Negative slicing
print(fruit[0:-3]) # print(fruit[0:len(fruit)-3])
print(fruit[0:len(fruit) - 3]) # Ap
print(fruit[-3:-1]) # pl
print(fruit[-3:]) #ple

#Quiz
nm = "Harry"
print(nm[-4:-2]) #ar

