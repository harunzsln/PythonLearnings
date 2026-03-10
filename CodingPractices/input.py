def getSquare(a):
    
    return a**2

#num int(input("Enter a number: "))
 #print("The square of", num, "is", getSquare(num))



v = float(input("Enter a value of voltage: "))
  
while True: 
    try:
        r = float(input("Enter a value of resistance: "))
        i = v / r
        break
    except ZeroDivisionError:
        print("Resistance cannot be 0.")

print("The current is: {}".format(i))


num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")