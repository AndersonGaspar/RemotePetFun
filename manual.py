from gpiozero import AngularServo
from time import sleep
import getch

# #MOTOR_Y = 11
# MOTOR_Y = 17
# #MOTOR_X = 13
# MOTOR_X = 27


def set_motors(self, motorx, motory):
    MOTOR_X = motorx
    MOTOR_Y = motory


servo2 = AngularServo(set_motors.MOTOR_Y, min_angle=-45, max_angle=90)
servo1 = AngularServo(set_motors.MOTOR_X, min_angle=-180, max_angle=180)

def posicao_inicial():
    servo1.angle = 0
    servo2.angle = 60

def move_direita():
    print(servo1.angle)
    if servo1.angle > -180:
        servo1.angle = servo1.angle - 15
    print(servo1.angle)
    # servo1.angle = 90
    # print(-90)
    sleep(1)

def move_esquerda():
    print(servo1.angle)
    if servo1.angle < 180:
        servo1.angle = servo1.angle + 15
    print(servo1.angle)
    # servo1.angle = -90
    # print(90)
    sleep(1)

def move_cima():
    print(servo2.angle)
    if servo2.angle > 15:
        servo2.angle = servo2.angle - 15
    print(servo2.angle)
    #servo2.angle = -90
    #print(-90)
    sleep(1)

def move_baixo():
    print(servo2.angle)
    if servo2.angle < 90:
        servo2.angle = servo2.angle + 15
    print(servo2.angle)    
    #servo2.angle = 90
    #print(90)
    sleep(1)


def le_tecla():
     while True:
         print('Digite w para movimentar para cima')
         print('Digite s para movimentar para baixo')
         print('Digite a para movimentar para esquerda')
         print('Digite d para movimentar para direita')
         print('Digite r para retornar ao menu anterior')
         tecla_comando = getch.getch()
         if tecla_comando == 'w':
             move_cima()
         if tecla_comando == 's':
             move_baixo()
         if tecla_comando == 'a':
             move_esquerda()
         if tecla_comando == 'd':
             move_direita()
         if tecla_comando == 'r':
             break
         else:
             print('\n Opcao incorreta, tente novamente!')

#posicao_inicial()
#le_tecla()

