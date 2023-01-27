import pyfirmata
from pyfirmata import Arduino
from pyfirmata import SERVO
from time import sleep

port = 'COM7'
pin = int(9)
board = pyfirmata.Arduino(port)
x = 0

board.digital[pin].mode = SERVO


def rotate_servo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)


rotate_servo(pin, 0)
sleep(1)

while x < 11:
    rotate_servo(pin, x * 18)
    sleep(0.1)
    x += 1

rotate_servo(pin, 0)
sleep(0.25)
rotate_servo(pin, 90)
sleep(0.25)
x = 0

while x < 6:
    rotate_servo(pin, x * 18)
    sleep(0.5)
    x += 1

while x < 11:
    rotate_servo(pin, x * 18)
    sleep(0.1)
    x += 1

rotate_servo(pin, 90)
sleep(0.5)
rotate_servo(pin, 0)
sleep(0.5)

    
# while True:
#     user_input = input("Input: ")
    # if (user_input.isdigit()):
    #     rotate_servo(pin, user_input)

    # if user_input == "180":
    #     for i in range(0, 180):
    #         rotate_servo(pin,i)
    
    # elif user_input == "90":
    #     for i in range(0, 90):
    #         rotate_servo(pin, i)

    # else:
    #     print("Error")

