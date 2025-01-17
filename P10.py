# Exercise for if - else statement
# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. 
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
if(hour>=0 and hour<12):
  print("Good Morning")
elif(hour>=12 and hour<17):
  print("Good Afternoon")
elif(hour>=17 and hour<0):
  print("Good Night")
