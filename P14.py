#Break and Continue Statements
for i in range(12):
  if(i == 10):
    break
  print("5 X", i + 1, "=", 5 * (i + 1))
print("Exit from the loop")
print("\n")

# Break = Exit the loop
# Continue = Exit the iteration

# Continue
for i in range(12):
  if(i==10):
    print("Skip the iteration")
    continue
  print("5 X", i, "=", 5 * i)