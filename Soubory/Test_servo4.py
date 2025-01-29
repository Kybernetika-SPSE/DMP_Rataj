import time
from machine import Pin, PWM, ADC
from servo import Servo

button = Pin(14, Pin.IN, Pin.PULL_DOWN)
tlacitko = Pin(10, Pin.IN, Pin.PULL_DOWN)
prvni = ADC(Pin(26))
servo = Servo(pin_id=15)

oto = 0
uhel = 0  
pos = 90
max = 50000

while True:   
    hlav = prvni.read_u16()
    servo.write(91)
    time.sleep_ms(100)   
    servo.write(100)
    time.sleep_ms(75)


    #print(oto*36)
    print(oto)
    print(hlav)
    print(max)
    oto = oto + 1
    if hlav<max:
        max = hlav
        uhel = oto
    if oto == 23:
        servo.write(91)
        break

uhel = (360/(oto-1))*uhel
print(uhel)
servo.write(65)
while True:
    if button.value() == 1:
        servo.write(91)
        break

