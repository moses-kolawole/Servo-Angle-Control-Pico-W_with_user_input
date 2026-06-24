import machine
from time import sleep as s
servopin = 15
servo = machine.PWM(machine.Pin(servopin))
servo.freq(50)
 
while True:
    angle = int(input('what angle do you desire? '))
    writeval = ((6553/180) * angle) + 1638
    servo.duty_u16(int(writeval))
    s(0.02)