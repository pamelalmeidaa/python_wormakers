# condições com if, elif e else em Python

idade = 55
e_menbro = True

if idade >= 60:
    if e_menbro:
        print("30% de desconto")
    else:
        print("20% de desconto")
elif idade >= 50:
    print("Vale compras com cashback")
else:
    print("Sem desconto")