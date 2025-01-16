# String Methods
# Strings are immutable
a = "Replit"
print(len(a))
print(a.upper())  #REPLIT
print(a.lower())  #replit
#rstrip()
b = "Program!!!!!"
print(b.rstrip("!"))  #Program
c = "!!!!!Program!!!!!"
print(c.rstrip("!"))  #!!!!Program; it strips only at ending
#replace()
print(a.replace("Replit", "Python"))  #replace replit with python
#split()
str1 = "Welcome to the Console!!!"
print(str1.split(" "))  #['Welcome', 'to', 'the', 'Console!!!']
#capitalize()
#It retuns only first character of the first word to the capital and turns the rest characters to small
str2 = "platform is great"
print(str2.capitalize())  #Platform is great
str3 = "PlatfOrm is great"  # capital O
print(str3.capitalize())  # Platform is great
#center()
str4 = "Welcome to the Console!!!"
print(str4.center(50))  #Welcome to the Console!!! in centre
print(len(str4))  #25
print(len(str4.center(50)))  #50
#count()
str5 = "Abracadabr"
print(str5.count("a"))
#endswith()
str6 = "Welcome to the Console!!!"
print(str6.endswith("!!!"))  #True
print(str6.endswith("to", 4, 10))  #True ; is "to" there between index 4 to 10
#find()
str7 = "He's name is Dan. He is an honest man."
print(str7.find("is"))  #10
print(str7.find("ishh"))  #-1; cause "ishh" is not there
#index()
#print(str7.index("ishh")) #Throws an error cause the string is not found
#isalnum()
str8 = "WelcomeToTheConsole"
print(str8.isalnum())  #True
#isalpha()
str9 = "welcome"
print(str9.isalpha())  #True
str10 = "Welcome12"
print(str10.isalpha())  #False
#islower()
str11 = "hello world"
print(str11.islower())  #True
#isprintable()
str12 = "We wish you a Merry Christmas"
print(str12.isprintable())  #True
str13 = "We wish you a Merry Christmas\n"
print(str13.isprintable())  #False; as there is "\n"
#isspace()
str14 = "        "
print(str14.isspace())  #True
#istitle()
# It only returns "True" if the first letter of each word of the string is capitalized
str14 = "Replit Is The Best Platform"
print(str14.istitle())  #True
#isupper()
str15 = "HELLO WORLD"
print(str15.isupper())  #True
#startswith()
str16 = "Python is an interpreted Language"
print(str16.startswith("Python"))  #True
#swapcase()
#Upper case to lower and vice-versa
str17 = "Python is an interpreted Language"
print(str17.swapcase())  #pYTHON IS AN INTERPRETED LANGUAGE
#title()
#It capitalizes each letter of the word within the string
str18 = "His name is Dan. Dan is an honest man."
print(str18.title())
