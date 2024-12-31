# patterns

totalrows = int(input("Enter the number of row:"))
for row in range(1,totalrows+1):
    for space in range(1, (totalrows-row)+1):
       print(" ", end="")
    for symbol in range(1, row+1):
       print("*", end="")
    print()
