import random 

yaziGelen = 0
turaGelen = 0

paraYuzeyi = ["Yazi", "Tura"]

atilacakPara = int(input("Kac defa para atilsin: "))

while atilacakPara > 0:
    paraUstu = random.choice(paraYuzeyi)
    if paraUstu == "Yazi":
        yaziGelen += 1
        print("Yazi geldi")
    else:
        turaGelen += 1
        print("Tura geldi")

    atilacakPara -= 1
print("Yazi gelme Sayisi: {}\nTura gelme Sayisi : {}".format(yaziGelen, turaGelen))
    