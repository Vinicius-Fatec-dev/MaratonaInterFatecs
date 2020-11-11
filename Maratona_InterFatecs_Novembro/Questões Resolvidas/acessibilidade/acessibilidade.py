linha1 = input().split(" ")
altura, comprimento, largura = linha1
altura = float(altura)
comprimento = float(comprimento)
largura = float(largura)
if altura > 0 and comprimento > 0 and largura > 0:
    inclinacao = (altura * 100) / comprimento
    if inclinacao <=8.334 and largura >= 0.80:
        print ("PROJETO SIMPLES")
    else:
        print ("PROJETO ESPECIAL")
else:
    print(" ")