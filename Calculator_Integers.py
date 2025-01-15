print ("Calculator")
x1 = input ("Number 1:")
x2 = input ("Number 2:")

total = int(x1) + int (x2)

str(total)
print (total)
ask = input ("want to add more? y/n")

if ask =="y":
    int(total)
    x3 = input ("Number 3:")
    totalx = total + int(x3)
    print (str(totalx))
    input ("Press Enter To Exit")

if ask =="n":
    input ("Press Enter To Exit")