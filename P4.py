#TypeCasting
a = "1"
b = "2"
print(a + b)  # 12
# The answer is 12 as a and b are strings
# The conversion of one data type into another data type is called type casting
# Explicit typecasting : done by the programmer
a = "1"
b = "2"
print(int(a) + int(b))  # 3
# Exercise
string = "15"
c = 10
string_num = int(string)
print(string_num + c)  # 25
# Implicit TypeCasting : done by the python interpreter
a = 0.1
b = 3
print(a + b)
# Exercise
a = 17.1
print(type(a))
b = 3
print(type(b))
sum = a + b
print(sum)
print(type(sum))
