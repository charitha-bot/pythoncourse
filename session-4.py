a=10
b=20
if a>8:
    if b>20:
        print('great')
    print('winner')

a=2
b=3
c=1
d = (a>b) and (a>c)
if d:
    print(a)
else:
    d=(b>c)
    if d:
        print(b)

a = 5
b = (a%10 == 0)
c = (a%5 == 0)
if b:
    print('divsible by 10')
elif c:
    print('divisible by 5')
else:
    print('neither 10 nor 5')

'''if 10>5:
    print("x")
else:
    print("y")
elif 5>10:
    print("z")''' # syntax error cause after else elif is there


a = 10
counter = 0
while counter<3:
    a = a+1
    print(a)
    counter = counter+1

a = 4
while counter<3:
    a = a+1
    print(a)
    counter = counter+1
print("end")

a = "python"
for i in a:
    print(i)

for i in range(3):
    print(i) # 0,1,2

for i in range(5,8):
    print(i) # 5,6,7

is_digit = '4748'.isdigit()
print(is_digit) #True

a = "10".isdigit()
print(a) #True

mobile = " 9704738292 "
mobile = mobile.strip()
print(mobile) #9704738292

a = "charitha."
name = a.strip(".")
print(name) #charitha

a = "teh cat and teh dog"
b = a.replace("teh", "the")
print(b) #the cat and the dog

url="https://onthegomodel.com"
is_secure_url = url.startswith("https://")
print(is_secure_url) #True









