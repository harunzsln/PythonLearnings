def tamSayıBolenleriDondur(inputNum): 
    divisors = []
    for i in range(1, inputNum + 1):
        if inputNum % i == 0:
            divisors.append(i)
    return divisors

inputNum = int(input("Bir tam sayı giriniz: "))
print(tamSayıBolenleriDondur(inputNum))