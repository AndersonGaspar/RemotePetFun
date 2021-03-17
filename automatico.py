import RPi.GPIO as GPIO
import time
import random
from gpiozero import AngularServo
from time import sleep
import time

# #MOTOR_Y = 11
# MOTOR_Y = 17
# #MOTOR_X = 13
# MOTOR_X = 27

def set_motors(self, motorx, motory):
    MOTOR_X = motorx
    MOTOR_Y = motory

servo2 = AngularServo(MOTOR_Y, min_angle=-45, max_angle=90)
servo1 = AngularServo(MOTOR_X, min_angle=-90, max_angle=90)

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

#posicao_inicial()
#auto()
