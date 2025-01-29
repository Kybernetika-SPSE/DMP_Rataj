from machine import Pin
from time import sleep_ms

pin = Pin("LED", Pin.OUT)

while True:
    pin.on()
    sleep_ms(100)
    pin.off()
    sleep_ms(500)