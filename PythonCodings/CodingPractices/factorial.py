num = int(
    input("Enter the positive integer for which you want to calculate the factorial: ")
)

factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print("The factorial of {} is {}".format(num, factorial))



