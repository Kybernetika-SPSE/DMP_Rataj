from machine import Pin, ADC
import utime

prvni = ADC(Pin(26))
druhy = ADC(Pin(27))

while True:
    jedna = prvni.read_u16()
    print("Prvni senzor "+str(jedna))
    utime.sleep_ms(150)
    dva = druhy.read_u16()
    print ("Druhy senzor "+str(dva))
    utime.sleep_ms(150)

    if jedna>dva:
        print("Na druhem je vetsi svetlo")
    else:
        print("Na prvnim je vetsi svetlo")
    
    utime.sleep_ms(500)
