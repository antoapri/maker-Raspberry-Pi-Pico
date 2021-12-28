import machine
import utime

led = machine.Pin(2, machine.Pin.OUT)
led1 = machine.Pin(3, machine.Pin.OUT)
led2 = machine.Pin(4, machine.Pin.OUT)
led3 = machine.Pin(5, machine.Pin.OUT)

led4 = machine.Pin(6, machine.Pin.OUT)
led5 = machine.Pin(7, machine.Pin.OUT)
led6 = machine.Pin(8, machine.Pin.OUT)
led7 = machine.Pin(9, machine.Pin.OUT)

while True:
     led.toggle()
     led1.toggle()
     led2.toggle()
     led3.toggle()
     utime.sleep(0.5)
     
     led4.toggle()
     utime.sleep(0.5)
     led5.toggle()
     utime.sleep(0.5)
     led6.toggle()
     utime.sleep(0.5)
     led7.toggle()
     utime.sleep(0.5)