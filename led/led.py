import machine
import utime

button = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(5, machine.Pin.OUT)

while True:
    if button.value() == 0:
        led.toggle()
        utime.sleep(0.5)