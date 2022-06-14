from machine import ADC
from machine import Pin
import time

OuterLightSensorPin = 'P15' 
InnerLightSensorPin = 'P14'

OuterLightPin = Pin(OuterLightSensorPin, mode=Pin.IN)  
InnerLightPin = Pin(InnerLightSensorPin, mode=Pin.IN) 

adc = ADC(bits=10)     # create an ADC object bits=10 means range 0-1024
                       # the lower value the less light detected
apinOuterLight = adc.channel(attn=ADC.ATTN_11DB, pin=OuterLightSensorPin)
                      # create an analog pin on P15;  attn=ADC.ATTN_11DB measures voltage from 0.1 to 3.3v
apinInnerLight = adc.channel(attn=ADC.ATTN_11DB, pin=InnerLightSensorPin)

def readOuterLight():
    result = 0     
    for i in range(10):
        result += apinOuterLight()
        time.sleep(1)
    result = result/10
    return result

def readInnerLight():
    result = 0     
    for i in range(10):
        result += apinInnerLight()
        time.sleep(1)
    result = result/10
    return result