from manual import set_motors, posicao_inicial, le_tecla, move_esquerda, move_direita, move_cima, move_baixo
from automatico import set_motors, posicao_inicial, auto
import getch

#MOTOR_Y = 11
MOTOR_Y = 17
#MOTOR_X = 13
MOTOR_X = 27

menu = 0
while True:
    print('1 - Modo automatico')
    print('2 - Modo manual')
    print('3 - Exit/Quit')
    menu=int(input('Escolha uma opcao: '))
    if menu == 1:
        print('\n Modo automatico')
        set_motors(MOTOR_X, MOTOR_Y)
        posicao_inicial()
        auto()
    elif menu == 2:
        print('\n Modo manual')
        set_motors(MOTOR_X, MOTOR_Y)
        posicao_inicial()
        le_tecla()
    elif menu == 3:
        print('\n Fim!')
        break
    else:
        print('\n Opcao incorreta, tente novamente!')

