import RPi.GPIO as GPIO
import time
import random
from gpiozero import AngularServo
from time import sleep
import time
import getch

#MOTOR_Y = 11
MOTOR_Y = 17
#MOTOR_X = 13
MOTOR_X = 27


servo2 = AngularServo(MOTOR_Y, min_angle=-45, max_angle=90)
servo1 = AngularServo(MOTOR_X, min_angle=-180, max_angle=180)


def posicao_inicial():
    servo1.angle = 0
    servo2.angle = 60
    
# alterar aqui depois para 10 minutos
fim = time.time()+30
def auto():
    try:
        while True:
            if time.time() >= fim:
                posicao_inicial()
                break
            i = random.randrange(-90, 90)
            servo1.angle = i
            print(i)
            time.sleep(1)
            i = random.randrange(-45,90)
            servo2.angle = i
            print(i)
            time.sleep(1)
    except KeyboardInterrupt:
        servo1.stop()
        servo2.stop()

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
#auto()
