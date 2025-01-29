import utime
from machine import Pin, ADC
from servo import Servo

button = Pin(14, Pin.IN, Pin.PULL_DOWN)
servo = Servo(pin_id=15)
prvni = ADC(Pin(28))




def hledani():
    while True:
        uznvm = 0
        oto = 0
        uhel = 0  
        pos = 90
        max = 100000
        if button.value() == 1:
            break
        else:    
            hlav = prvni.read_u16()
            servo.write(pos)
            utime.sleep_ms(500)
            pos = pos + 8    
            servo.write(pos)
            utime.sleep_ms(100)
            pos = pos - 8
        
            #print(hlav)
            oto = oto + 1
            if hlav<max:
                max = hlav
                uhel = oto
                uhel = "{:.1f}".format(uhel)

    pos = 50
    servo.write(pos)
    #time.sleep_ms(650)
    if button.value() == 1:
        pos = 90
        servo.write(pos)

    uznvm = 360/oto
    uhel = uhel * uznvm
    pos = 91
    servo.write(pos)
    print(oto)
    print("nejvetsi svetlo")
    #print(max)
    print("na uhlu")
    print(uhel)
    return uhel

hledani()
print(str(uhel))
