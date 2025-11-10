num = int(input("Enter a number: "))

counter = 2

prime_numbers = []

while num > 1:
    prime_numbers.append(num)
    while counter < num:
        if num % counter == 0:
            prime_numbers.remove(num)
            break
        counter += 1
    counter = 2
    num -= 1

print(prime_numbers)
