def ebob(a, b):
    enKucukSayi = min(a, b)
    enBuyukOrtakBolen = 1

    for i in range(1, enKucukSayi + 1):
        if a % i == 0 and b % i == 0:
            enBuyukOrtakBolen = i

    print(f"{a} ve {b} sayilarinin EBOB'u: {enBuyukOrtakBolen}")

sayi1 = int(input("Birinci sayiyi girin: "))
sayi2 = int(input("Ikinci sayiyi girin: "))
ebob(sayi1, sayi2)
