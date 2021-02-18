from manual import posicao_inicial, le_tecla, move_esquerda, move_direita, move_cima, move_baixo
#from automatico import posicao_inicial, auto
import getch

#def tecla():
#    while True:
#        tecla_comando = getch.getch()
#        if tecla_comando == 'w':
#            move_cima()
#        if tecla_comando == 's':
#            move_baixo()
#        if tecla_comando == 'a':
#            move_esquerda()
#        if tecla_comando == 'd':
#            move_direita()

menu = 0
while True:
    print('1 - Modo automatico')
    print('2 - Modo manual')
    print('3 - Exit/Quit')
    menu=int(input('Escolha uma opcao: '))
    if menu == 1:
        print('\n Modo automatico')
        posicao_inicial()
        auto()
    elif menu == 2:
        print('\n Modo manual')
        posicao_inicial()
        le_tecla()
    elif menu == 3:
        print('\n Fim!')
        break
    else:
        print('\n Opcao incorreta, tente novamente!')

