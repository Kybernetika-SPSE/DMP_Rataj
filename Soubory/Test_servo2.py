import time
from machine import Pin, PWM, ADC

prvni = ADC(Pin(26))
pwm = PWM(Pin(15))

pwm.freq(25)
def setServoCycle (position):
    pwm.duty_u16(position)

oto = 0
uhel = 0  
pos = 5
max = 50000

while True:   
    hlav = prvni.read_u16()
    setServoCycle(pos)
    time.sleep_ms(500)
    pos = pos + 10    
    setServoCycle(pos)
    time.sleep_ms(25)
    pos = pos - 10

    #print(oto*36)
    print(oto)
    print(hlav)
    oto = oto + 1
    if hlav<max:
        max = hlav
        uhel = oto*36
    if oto == 10:
        oto = oto - 10
        pos = 5
        setServoCycle(pos)
        print("nejvetsi svetlo =")
        print(max)
        print("na uhlu")
        print(uhel)
        break
