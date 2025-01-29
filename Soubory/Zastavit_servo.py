import time
from servo import Servo
servo = Servo(pin_id=15)

servo.write(80)
time.sleep(1)
servo.write(91)
