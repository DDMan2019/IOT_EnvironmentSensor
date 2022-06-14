import time
import pycom
import machine
from machine import I2C
from machine import Pin

import led
import lightSensor
import DHT11Sensor
import pybytesClient



print("Waking up")

pycom.heartbeat(False)

sleepMinututes = 10
(wake_reason, gpio_list) = machine.wake_reason()


def readSensorData():
    time.sleep(1)     # Just to get it some slack starting up

    innerLight = lightSensor.readInnerLight()
    outerLight = lightSensor.readOuterLight()
    dht = DHT11Sensor.readDHT()
    temp = dht.temperature
    humidity = dht.humidity
    
    print('readInnerLight:', innerLight)
    print('readOuterLight:', outerLight)
    print('Temperature', temp)
    print('humidity',humidity)
    return [innerLight,outerLight,temp,humidity]



sensorData = readSensorData()

pybytesClient.sendData(sensorData)
time.sleep(10) # Device needs some time to send the data before going to sleep
print("Device running for: " + str(time.ticks_ms()) + "ms")
print("Remaining sleep time: " + str(machine.remaining_sleep_time()) + "ms" )
print("Goodnight")

machine.deepsleep((1000*60) * sleepMinututes) #sleep for 10 minutes