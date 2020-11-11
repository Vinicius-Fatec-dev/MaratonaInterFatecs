Linha = input().split(" ")
N = int(Linha[0])
Q = int(Linha[1])
Peca = []
Cont = 1
Soma = 0
if 1 <= N <= 10 ** 5 and 1 <= Q <= 10 ** 3:
    while Cont <= Q:
        x = int(input())
        Peca.append(x)
        if x < N:
            Soma += x
            if Soma == N:
                print('SIM')
        Cont += 1
    if N in Peca:
        Soma = N
        print('SIM')
    if Soma > N or Soma < N and N not in Peca:
        print('NAO')