def ekok(a, b):
    ekok = a*b

    for num in range(ekok, max(a, b)-1,-1):
        if num % a == 0 and num % b == 0:
            ekok = num
    return ekok

firstNum = int(input("Enter the first number: "))
secondNum = int(input("Enter the second number: "))
print(ekok(firstNum, secondNum))