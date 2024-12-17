import palavras, funcoesJogo

jogo = True
letras = []
pontuacaoAtiva = 0
pontuacaoTotal = 0
erros = 1

palavrasJogo = palavras.palavras()

while jogo:
    palavra = funcoesJogo.sortear_palavra(palavrasJogo)
    palavraAtiva = True
    if erros > 0:
        erros -= 1
    print(f'Pontuação total: {pontuacaoTotal}\nErros: {erros}')
    while palavraAtiva:
        exibirPalavra = funcoesJogo.exibidor(letras, palavra)
        print (exibirPalavra)
        letra = input('Digite uma letra: ').strip()
        if len(letra) > 1:
            print('Letra invalida')
            continue
        acerto = funcoesJogo.verificarLetra(letra, palavra)
        if (acerto) and (letra not in letras):
            pontuacaoAtiva += 1
            pontuacaoTotal += 1
            letras += letra
        elif(not acerto):
            erros += 1
        if (pontuacaoAtiva) >= (funcoesJogo.qtdLetras(palavra)):
            exibirPalavra = funcoesJogo.exibidor(letras, palavra)
            print(f'\nVocê acertou a palavra "{exibirPalavra}"\n')
            letras = []
            pontuacaoAtiva = 0
            palavraAtiva = False
        if erros >= 5:
            print(f'Fim de jogo sua pontuação final foi: {pontuacaoTotal}')
            jogo = False
            break