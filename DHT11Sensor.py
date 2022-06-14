import time
from machine import I2C
from machine import Pin
from dht import DHT # https://github.com/JurassicPork/DHT_PyCom

th = DHT(Pin('P23', mode=Pin.OPEN_DRAIN), 0)
time.sleep(2)

def readDHT():
    result = th.read()
    while not result.is_valid():
        time.sleep(.5)
        result = th.read()
    return result


    