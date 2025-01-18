# Match case statements in python
x = int(input("Enter the value of x:"))
match x:
    case 0:
      print("x is zero")
    case 4:
      print("case is 4")
    case _:
      print(x)
# The main idea is to compare a variable to the patterns. Here the patterns are cases and the variable is x.

y = int(input("Enter the value of y:"))
match y:
     case _ if y!=90:
           print(y,"is not 90")
     case _ if y!=80:
           print(y,"is not 80")
     case _:
           print(y)