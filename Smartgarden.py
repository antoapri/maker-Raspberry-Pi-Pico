import machine
import utime

MoistureSensor = machine.ADC(26)            #GP pin Assign
Pump = machine.Pin(27, machine.Pin.OUT)

while True:
    RH = MoistureSensor.read_u16() 
    Percentage = (100-(RH/65535.00)*100)    #Conversion percentage
    print(Percentage)
    utime.sleep(2)
    if Percentage < 80:                     #kelembaban kurang dari 80% Pump )On
        led.value(1)
        Pump.value(1)
        utime.sleep(5)
        Pump.Value(0)
        utime.sleep(2)
    else :                                   #kelembaban lebih dari 80% Pump Off
        led.value(0)
        Pump.value(0)
