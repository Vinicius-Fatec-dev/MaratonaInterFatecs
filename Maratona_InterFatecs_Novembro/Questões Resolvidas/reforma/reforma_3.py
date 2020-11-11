Linha = input().split(" ")
N = int(Linha[0])
Q = int(Linha[1])
x = input().split()
Peca = []
O = 0
Conver = 0
Soma = 0
while O <= len(x) - 1:
    Conver = int(x[O])
    Peca.append(Conver)
    if Conver < N:
        Soma += Conver
        if Soma == N:
            print("SIM")
    O += 1
if N in Peca:
    Soma = N
    print("SIM")
if Soma > N or Soma < N and N not in Peca:
    print('NAO')
