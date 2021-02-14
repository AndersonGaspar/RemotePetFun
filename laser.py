import RPi.GPIO as GPIO
import time
import random
#import getch

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)



GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
#GPIO.setup(7, GPIO.OUT)

servo1 = GPIO.PWM(11, 70)
servo2 = GPIO.PWM(12, 50)


servo1.start(7.5)
servo2.start(7.5)

#local1 = servo1.ChangeDutyCycle(6.5)
#local2 = servo1.ChangeDutyCycle(11.5)


try:
    while True:
        i = random.randrange(4,12)
        servo1.ChangeDutyCycle(i)
        print(i)
        time.sleep(4)
        i = random.randrange(3,11)
        servo2.ChangeDutyCycle(i)
        print(i)
        time.sleep(4)
        i = random.randrange(4,12)
        servo1.ChangeDutyCycle(i)
        print(i)
        time.sleep(4)
        i = random.randrange(3,11)
        servo2.ChangeDutyCycle(i)
        print(i)
        time.sleep(4)
except KeyboardInterrupt:
    servo1.stop()
    servo2.stop()
    GPIO.cleanup()