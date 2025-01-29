from machine import Pin, ADC
import time

prvni = ADC(Pin(26))
druhy = ADC(Pin(27))

while True:
    jedna = prvni.read_u16()
    #print("Prvni senzor")
    print(jedna)
    time.sleep_ms(150)
    #dva = druhy.read_u16()
    #print ("Druhy senzor")
    #print(dva)

    time.sleep_ms(150)
    #if jedna>dva:
    #    print("Na druhem je vetsi svetlo")
    #else:
    #    print("Na prvnim je vetsi svetlo")
    #time.sleep_ms(200)
       