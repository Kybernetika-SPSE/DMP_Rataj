import utime
from machine import Pin, ADC
from servo import Servo

button = Pin(14, Pin.IN, Pin.PULL_DOWN)
servo = Servo(pin_id=15)
trig = Pin(21, Pin.OUT)
echo = Pin(20, Pin.IN)
pravej = ADC(Pin(26))
levej = ADC(Pin(27))
hlavni = ADC(Pin(28))
DCApos = Pin(13, Pin.OUT)
DCApro = Pin(12, Pin.OUT)
DCBpro = Pin(11, Pin.OUT)
DCBpos = Pin(10, Pin.OUT)

uznvm = 0
oto = 0
uhel = 0  
pos = 90
max = 100000
dis = 100


while True: 
    while True:   
        hlav = hlavni.read_u16()
        servo.write(91)
        utime.sleep_ms(100)   
        servo.write(100)
        utime.sleep_ms(75)

        #print(oto)
        #print(hlav)
        #print(max)
        oto = oto + 1
        if hlav<max:
            max = hlav
            uhel = oto
        if oto == 23:
            servo.write(91)
            break

    uhel = (360/(oto-1))*uhel
    servo.write(65)
    while True:
        if button.value() == 1:
            servo.write(91)
            break   
    print(uhel)
    utime.sleep(1)
    #otočit se na tento uhel
    if uhel < 180:
        DCApos.value(1)
        DCApro.value(0)
        utime.sleep_ms(10*uhel)
        #Zatoč doleva
    elif uhel > 180:
        uhel = 360-uhel
        DCBpos.value(1)
        DCBpro.value(0)
        utime.sleep_ms(10*uhel)
        #Zatoč doprava

    #Jed dokud nejsme 5 cm od překážky
    while dis <= 5:
        #Jak blízko jsem k překážce
        trig.low()
        utime.sleep_us(2)
        trig.high()
        utime.sleep_us(5)
        trig.low()
        while echo.value() == 0:
            soff = utime.ticks_us()
        while echo.value() == 1:
            son = utime.ticks_us()

        timepass = son - soff
        dis = (timepass * 0.0343) / 2
        dis = "{:.1f}".format(dis)  
            
        print(dis+ " cm")

        #Jedu mimo kurz?
        R = pravej.read_u16()
        utime.sleep_us(10)
        L = levej.read_u16()
        utime.sleep_us(10)

        if R>L:
            if ((R-L)>1000):
                print("Zatoč doleva")
            elif ((R-L)>500):
                print("Zatoč lehce doleva")          
        elif L>R:
            if ((L-R)>1000):
                print("Zatoč doprava")
            elif ((L-R)>500):
                print("Zatoč lehce doprava")
    utime.sleep(300)

