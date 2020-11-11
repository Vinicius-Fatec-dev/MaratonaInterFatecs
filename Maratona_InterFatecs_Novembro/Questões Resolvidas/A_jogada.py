'''  numeroDigitado = int(input("Digite um número de jogadas: "))
contador = 0
luisa = 0
antonio = 0

while contador <= numeroDigitado:
    if contador == numeroDigitado:
        break
    dadoJogadoLuisa = int(input("Jogue o dado Luisa: "))
    if dadoJogadoLuisa <= 6:
       luisa = dadoJogadoLuisa + luisa 
    if dadoJogadoLuisa == 6:
        if contador == numeroDigitado:
            break
        
        else:
            while True:
                dadoJogadoLuisa = int(input("Jogue novamente o dado: "))
                if dadoJogadoLuisa == 6: 
                    luisa = dadoJogadoLuisa + luisa
                if dadoJogadoLuisa != 6:
                    luisa = dadoJogadoLuisa + luisa
                    contador += 1
                    break
    contador += 1        
            
    dadoJogadoAntonio = int(input("Jogue o dado Antonio: "))
    if dadoJogadoAntonio <= 6:
        antonio = dadoJogadoAntonio + antonio
    if dadoJogadoAntonio == 6:
        if contador == numeroDigitado:
            break
        
        else:
            while True:
                dadoJogadoAntonio = int(input("Você ganhou uma nova jogada: "))
                if dadoJogadoAntonio == 6:
                    antonio = dadoJogadoAntonio + antonio
                if dadoJogadoAntonio != 6:
                    antonio = dadoJogadoAntonio + antonio
                    contador += 1
                    break
    contador += 1
    
if luisa > antonio:               
    print("LUISA", luisa) 
    
if antonio == luisa:
    print("EMPATE")
    
if antonio > luisa:
    print("ANTONIO", antonio)
    
'''
jogadas =  int(input())
contador = 1 
somaluisa = 0 
somaantonio = 0
contajogada = 1

if jogadas >=2 and jogadas <=100:
    while contador <= jogadas:
            if contajogada <=jogadas:
                jogador1 = int(input("Jogue o dado Luisa: "))
                somaluisa = jogador1 + somaluisa
                contador = contador +1
                contajogada = contajogada + 1
                while jogador1 == 6 and contador <=jogadas:
                    jogador1 = int(input("Jogue o novamente Luisa: "))
                    somaluisa = jogador1 + somaluisa
                    contador = contador +1
                    contajogada = contajogada + 1
            if contajogada <=jogadas:
                jogador2 = int(input("Jogue o dado Antonio: "))
                somaantonio = jogador2 + somaantonio
                contador = contador +1
                contajogada = contajogada + 1
                while jogador2 == 6 and contador <=jogadas:
                    jogador2 = int(input("Jogue o novamente Antonio: ")) 
                    somaantonio = jogador2 + somaantonio
                    contador = contador +1
                    contajogada = contajogada + 1
    if (somaantonio > somaluisa):
        print ("ANTONIO", somaantonio)
    elif (somaluisa > somaantonio):
        print ("LUISA", somaluisa)
    else:
        print ("EMPATE", somaluisa)
else: 
    print ("Número de jogadas incorretas !!!")