import machine
import utime

potentiometer = machine.ADC(27)
led = machine.PWM(machine.Pin(15))
led.freq(1000)

while True:
 led.duty_u16(65535)