import machine
import utime

potentiometer = machine.ADC(26)
conversion_factor = 3.3 / (65535)
led = machine.Pin(6, machine.Pin.OUT)
led1 = machine.Pin(7, machine.Pin.OUT)

while True:
    voltage = potentiometer.read_u16() * conversion_factor
    print(voltage)
    utime.sleep(2)
    if voltage >= 2:
        led.value(1)
        led1.value(1)
    else :
        led.value(0)
        led1.value(0)