import machine
import utime

button = machine.Pin(20, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(2, machine.Pin.OUT)
led1 = machine.Pin(6, machine.Pin.OUT)
led2 = machine.Pin(10, machine.Pin.OUT)

button1 = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_DOWN)
led3 = machine.Pin(5, machine.Pin.OUT)
led4 = machine.Pin(9, machine.Pin.OUT)
led5 = machine.Pin(13, machine.Pin.OUT)

button2 = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_DOWN)
led6 = machine.Pin(26, machine.Pin.OUT)
led7 = machine.Pin(27, machine.Pin.OUT)
led8 = machine.Pin(28, machine.Pin.OUT)


while True:
#button ke1
    if button.value() == 0:
         print("button 20")
         utime.sleep(0.1)
         led.value(1)
         led1.value(1)
         led2.value(1)
    else :
        led.value(0)
        led1.value(0)
        led2.value(0)
#button ke2
    if button1.value() == 0:
         print("button 21")
         utime.sleep(0.1)
         led3.value(3)
         led4.value(3)
         led5.value(3)
    else :
        led3.value(0)
        led4.value(0)
        led5.value(0)
#button ke3
    if button2.value() == 0:
         print("button 22")
         utime.sleep(0.1)
         led6.value(1)
         led7.value(1)
         led8.value(1)
    else :
        led6.value(0)
        led7.value(0)
        led8.value(0)
