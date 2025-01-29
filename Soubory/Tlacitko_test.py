import time
from machine import Pin

button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    print(button.value())
    time.sleep_ms(100)
    if button.value() == 1:
        print("Button is pressed")
        break
