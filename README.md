
Indoor environment sensor (outdoorlight, indoorlight, humidity and temperature)
======================================

By Daniel Jansson (dj222mi)

I have decided to make a IoT device that measures indoor and outdoor light, and the temperature and humidity indoors.
This device will startup once every 15 minutes to read sensor data and then send this to an online platform which will display the data and after that the device will go to sleep. It must be placed at a window to receive a correct data.

If you are familiar with programming especially with Python and have some basic experience with sensors, then this project should be relatively easy to assemble and implement once you know how to do it. 
This project will approximately take around 2-3 hours to assemble and implement.


### [ ](https://hackmd.io/@lnu-iot/iot-tutorial#Objective "Objective")Objective

I have decided to do this project as a good introduction to IoT.
The purpose of this project is to know how much sunlight I get in the apartment and to know the temperature and relative humidity indoors.

Some insights that this project has already given me is that I could the first weeks see on the graphs that are drawn from the data that the nights are getting shorter and shorter each day as midsummer is coming.

I have also learned that I get sunlight directly on the window at 17.00 which can be clearly seen on the graph below as the graph goes straight up. That happens because the sun shines directly at the light sensor.

On the graph below you can clearly see the difference when the sun went up, the night before was a little longer than its latest day.
![](https://i.imgur.com/DIyWYl1.png)

Another insights that I have drawn from measuring the temperature and humidity is that I have a pretty comfortable temperature indoor compared with outside that is right now at 30 degrees warm while indoor we have almost constant at 26 degree.

But when we add in the relative humidity I have discovered that with a higher humidity for example around 60% it was very warm indoor, I have learned that by opening the door to be balcony I could see on the graph that the humidity went down a bit which made it cooler.

Relative humidity is about how much water vapor there is in the air and the unit of measure we will use in this tutorial is in percent. [[1](#Footnotes)]


### [ ](https://hackmd.io/@lnu-iot/iot-tutorial#Material "Material")Material

To build this project. I have chosen the following materials
 * PyCom - LoPy4 (https://pycom.io/product/lopy4/)
 * Pycom Expansion Board (https://pycom.io/product/expansion-board-3-0/)
 * 2x Photoresistors (https://www.electrokit.com/produkt/fotomotstand-cds-2-5-kohm/)
 * 2x Resistors(10K Ohm) and at least 10 cables (Electrokit)
 * DHT11 Digital Temperature and moisture sensor (https://www.electrokit.com/produkt/digital-temperatur-och-fuktsensor-dht11/)
 * Breadboard (https://www.electrokit.com/produkt/kopplingsdack-400-anslutningar/)
 * USB Cable which you can connect to PC and to a powersource.
 
 | Item | Link | Estimated Price(SEK)
 | --- | --- | ---
 | Pycom - LoPy4 | [Pycom](https://pycom.io/product/lopy4/)  | 388
 | Pycom Expansion Board| [Pycom](https://pycom.io/product/expansion-board-3-0/) | 181 |
 | 2x Photoresistors(560 Ohm) 10k Ohm is recommended  | [ElectroKit](https://www.electrokit.com/produkt/fotomotstand-cds-2-5-kohm/) | 8 |
 | DHT11 Digital Temperature and moisture sensor| [ElectroKit](https://www.electrokit.com/produkt/digital-temperatur-och-fuktsensor-dht11/) | 49 |
 |Breadboard  | [ElectroKit](https://www.electrokit.com/produkt/kopplingsdack-400-anslutningar/) | 59 |
 |  Micro USB Cable | [Kjell&Co](https://www.kjell.com/se/produkter/dator/kablar-adaptrar/usb/usb-kablar/micro-usb-kabel-1-m-p68687) | 100 |
  | Total cost | |785

If you want you can buy a batterypack from [ElectroKit](https://www.electrokit.com/produkt/batterihallare-3xaaa-med-strombrytare-och-jst-kontakt/) they are very cheap but I would recommend to buy a lipo battery with at least 10k mAh. The reason for this will be explained in later in this tutorial.

I have chosen to use Pycom LoPy4 which is a microcontroller dedicated for IoT.
It is designed to run in Micropython which is a programming language optimized to run on a microcontroller. It is based on Python

The Expansion board is used to connect the Lopy4 and sensors plus this gives power to the Lopy4 via usb or battery. This one is used to connect to the computer for developing the microcontroller.

The photoresistors that are needed are also known as a light-dependent resistor which is a component that works like a sensor. When it receives light then the resistance will decrease letting more electrons to pass through. When it receives more less light then the resistance will be higher and less electrons will pass through. This will the Lopy4 receive as analog data in measured voltage.

DHT11 is a module that has built in temperature and humidity sensor. The big difference compared with the photoresistor is that it has 3 pins, one for ground and one for power. The third pin connects to the expansion board that will send the value as bytes compared with the photoresistor that only gives the value as voltage.

To connect all this, it is recommended to use a breadboard because then connecting everything will be much easier.
 

### [ ](https://hackmd.io/@lnu-iot/iot-tutorial#Computer-setup "Computer-setup")Computer setup

In this tutorial I have chosen to use VSCode as this is my primary IDE for developing applications at my work.

The first thing that you need to do is to install a plugin called PyMakr, you can find this in this [link](https://pycom.io/products/supported-networks/pymakr/) or you can download it though VSCode or Atom. Those two are the only IDE’s that supports PyMakr.

PyMakr is a plugin that enables the user to connect the Lopy4 with the PC, when PyMakr is installed a console will be shown on the IDE which is used for debugging, running, or uploading the code to the Lopy4.

I am using Windows 10 mainly so this tutorial is aimed for Windows users but VSCode can be run on Linux machines also and the PyMakr plugin should likely work on it without many issues.

The Expansion Board needs to be updated with the latest firmware to ensure it will communicate with Pybytes which we will use to display the data. To do that please follow this [guide on how to update the firmware](https://docs.pycom.io/updatefirmware/device/).


### [ ](https://hackmd.io/@lnu-iot/iot-tutorial#Putting-everything-together "Putting-everything-together")Putting everything together

To begin with you must always ensure that the breadboard or the Lopy4 is not connected to any power supply while connecting the cables and the sensors.

The cables usually have different colors, this is just for identifying which cable that goes to were. You can pick any colors you want, in this tutorial I have for example chosen to use green cables that is connected to the pins on the Expansion board for reading values, while for black and white cables they are for giving the sensors electricity.

Let’s start by first placing the sensors on the breadboard. Start by first placing the first two photoresistors. They have two pins, for the first one set one pin at 2E and the other pin at 3E on the breadboard.
The other photoresistor you can place it with one pin at 8E and the other pin at 9E.

Next step is to connect the cables for the photoresistors and they both need their own resistor, so they don’t get too much voltage. In my tutorial I have used a 560 Ohm but for those Photoresistors that I bought from ElectroKit it is recommended to use 10K Ohm for, but I haven’t encountered any problem with the resistance I have used yet.

The first resistor needs to be connected from any hole on the minus pole side to the same row as the 3E and 9E is located at. Do the same for the other resistor.

Once that is done, you can decide which one should measure light from outdoor and one from indoors by bending the photoresistor so one faces the window and one facing into the room.

Now we can connect the cables to the photoresistors. We first need to plug one cable from any hole on the plus pole side to same row as 2E. The other cable we do the same but this one should be at the same row as 8E.

Next step is to connect the green cables that is for sending analogue data to the LoPy4. Connect one cable from same row as one of the resistors, it should be on the hole after the resistor. This you will plug into the Expansion Board in the pin called P15 which is for the outer light.

Do the same for the other pin, plug it on the hole next to the second resistor and plug it to the pin called P14 which is for inner light.

Now we are ready for the DHT11. This one has a built-in resistance, so we don’t need to think about plugging in any resistors. Place it at the breadboard so that it is placed in parallel to the side of the breadboard. Connect a red cable from the minus pole side to the hole that is on the same row as the right pin on the DHT11. After that, connect a blue cable from the plus pole side to the hole that is on the same row as the pin in the middle of DHT11.


Finally you can connect the green cable from the same row as the left pin on the DHT11 to P23.
If you have done everything right, then everything should look like this:
![](https://i.imgur.com/kfB3pPu.jpg)

As an extra note, I have chosen to disable the led indicator on the expansion board that gets lit every time it measures something. This is possible to do by using a hack in the code that disables the Led but you can also physically disable it by removing the jumper that is beside next to a label called LED on the expansion board. You can just put it to the side like this picture.

This is not necessary to do and if you chose to have the led light on it will not affect the outcome of this project.

![](https://i.imgur.com/ApPeE9F.jpg)

### [ ](https://hackmd.io/@lnu-iot/iot-tutorial#Powerconsumption "Powerconsumption")Power Consumption
If you decide to use a battery, then it is important to consider the power consumption. 
I would recommend using a lipo battery as that will last for almost one month given that you are using Sigfox or lora that has lower power consumption than Wi-Fi. Should you decide to not use battery then you can skip this entire section.

The lopy4 device is consuming 30 mAh with no radios connected but with Sigfox connected then it will consume 60 mAh and Wi-Fi consumes 107 mAh which is why I recommend using Sigfox. In deep sleep it will consume 19.5 mAh [[2](#Footnotes)].

As the device will sleep every 15 minutes and spend 20 seconds awake then you can calculate the power consumption by following these calculations

So first we know that the lopy4 will use 19.5 mAh per hour when it is asleep, so we need to divide this by 60 so we know how much battery power it consumes per minute, the same goes with how much it uses when awake so then we get:
```
sleep_draw = 19.5/60 
awake_draw = 60/60

sleep_draw = 0.325
awake_draw = 1
```
Now we need to know how long time it is awake of the total time. We will be sleeping for 15 minutes and then wake up for 21 seconds and then back to sleep for 15 minutes. We will reduce this to seconds so 15 minutes will be 900 seconds.
```
awake_percentage = 21/(900 + 21)
awake_percentage = 0.023
```
We need to know how many minutes of an hour that the device is awake, the same goes for how many minutes of an hour it is asleep, then we will subtract 60 minutes with how many total minutes it is awake.
```
awake_minutes = 0.023 * 60
awake_minutes = 1.37

sleep_minutes = 60 - 1.37
sleep_minutes = 58.63
```
This means that the device will be awake for total 1.37 minutes and asleep for 58.63 minutes in one hour.

Now we can get the cost in mAh when active and when asleep. We need to multiply how much mAh it takes per minute when awake times how many minutes it is awake, the same is for when it is asleep, so we will calculate like this

```
active_cost = awake_draw * awake_minutes
sleep_cost = sleep_draw * sleep_minutes

active_cost = 1 * 1.37 
sleep_cost = 0.325 * 58.63

active_cost = 1.3680781758957654
sleep_cost = 19.055374592833875
```
Now we know how much is costs so finally we can add this together:
```
total mA per hour = active_cost + sleep_cost
```
Which means that this device will consume 20.42 mAh per hour and so I would recommend using lipo battery of at least has 10000 mAh of capacity, then the lopy4 will be working for a little bit over 20 days.

Here are the final calculations:
```
sleep_draw = 19.5/60 #per minute
awake_draw = 60/60

sleepseconds = 900
awakeseconds = 21
awake_percentage = awakeseconds/(sleepseconds + awakeseconds) 

awake_minutes = awake_percentage * 60 
sleep_minutes = 60 - awake_minutes

active_cost = awake_draw * awake_minutes
sleep_cost = sleep_draw * sleep_minutes

total_cost = active_cost + sleep_cost
```

### [ ](https://hackmd.io/@lnu-iot/iot-tutorial#Platform "Platform")Platform

I have decided to use Pybytes as it is a free platform as this is made for Pycom devices. It is hosted on the cloud, so you need to register an account for this. It works fine but the downside of this is that it will only store data for less than 1 month.

The platform can be accessed [here](https://pybytes.pycom.io/)

Make sure to register your pycom device there and update the firmware otherwise you may not get any data.

The code for sending data to Pybytes is very easy and straightforward but if you want you can send the data to other platforms as well. That can be done via Pybytes that then forward the data to the platform that you want to use, but if you don’t want to use Pybytes at all then you may have to rewrite the provided code in this tutorial.
So for ease of access I have decided to use Pybytes as the chosen platform to display data.

### [ ](https://hackmd.io/@lnu-iot/iot-tutorial#The-code "The-code")The code

The code is written in MicroPython. It is split into 4 files. What the code does is that it will read data from the two photoresistors and then it will read the temperature and humidity from the DHT11.

After this is done it will send the data to Pybytes and then it will go to sleep mode for 15 minutes and after 15 minutes it will wake up to do the same code again.

Let’s first start with the light Sensors. This file contains two similar functions, one for measuring the light outdoors and the other one for measuring the light indoors.

We want to get the mean value of the light which is why we get reading 10 times with 1 second pause and then divide it by 10.

Name this file 
`lightSensor.py`
```python=
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
```

The next step is to create the code for the DHT11 sensor. This will get reading from an external DHT library which you can get from [here](https://github.com/JurassicPork/DHT_PyCom/blob/master/dth.py)
You have to download the file and save it in a new folder called lib that should be in same folder as in your project. Below is the code for reading the data from DHT11

`DHT11Sensor.py`
```python=
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
```

Now we can create a new file called `main.py`  this is the main code that will use the code from the sensors and the code for the pybytesclient. This is where all comes together.
`main.py`
```python=
import time
import pycom
import machine

from machine import I2C
from machine import Pin

import lightSensor
import DHT11Sensor
import pybytesClient

print("Waking up")

pycom.heartbeat(False) # This is to disable the blue flashing light on the lopy4.

sleepMinututes = 15

def readSensorData():
    time.sleep(1)  # Just to get it some slack starting up

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

# This will send the sensordata to pybytes which we will go through in the next file.
pybytesClient.sendData(sensorData)

time.sleep(10) # The device needs some time to send the data before going to sleep.

machine.deepsleep((1000*60) * sleepMinututes) # sleep for 10 minutes
```

Now we can implement the code for sending the data to Pybytes.
What this code does is that it will create a connection to Pybytes when the this file is read.

It has a function that is called from main that is named sendData which will take an array of values and then send it in a loop to Pybytes.
We will use this name:
`pybytesClient.py`
```python=
import time
import pycom
import machine

from machine import I2C
from machine import Pin
from _pybytes import Pybytes
from _pybytes_config import PybytesConfig

#Read connection info
conf = PybytesConfig().read_config()
pybytes = Pybytes(conf)
pybytes.start()
pybytes.send_ping_message()
  
def sendData(arrData): #Send each data as a signal to pybytes
    n = 1
    for data in arrData:
        pybytes.send_signal(n,data)
        n += 1
```

Now the code is ready to be uploaded on the Lopy4 device. But if you want to disable the led light indicator, you can as mentioned earlier physically disable it or you can do it via code.
The difference doing this via code is that it will only show the led light when it is booting up and when the code runs its off.

I recommend placing this code in `main.py `after the line that says `pycom.heartbeat(False)`

```python=
# This is for turning off the led indicator on the expansion board
led = Pin('P9', mode = Pin.OUT)
button = Pin('P10', mode = Pin.IN)
led.value(1) 
```
To upload the code to Lopy4 you need to have PyMakr installed as a plugin in VsCode otherwise you can’t upload the code to the Lopy4.
Make sure you have the usb-cable connected from the expansion board to the computer.

The PyMakr plugin in Vscode should automatically detect this. Once it is detected there should be a button below the console that says “Upload”, click on it and then VsCode will upload the code to Lopy4 and then it will boot up and execute the code.

### [ ](https://hackmd.io/@lnu-iot/iot-tutorial#Transmitting-the-data--connectivity "Transmitting-the-data--connectivity")Transmitting the data / connectivity

I have decided to use Sigfox as a way to transmit data as this consumes less energy and it has a longer range compared with Wi-Fi[[2](#Footnotes)] and this was the only connection that was not Wi-Fi that worked on my Lopy4. The nearest lora antennas was too far away from my home but I was lucky that I could connect to Sigfox instead.

I wanted to use Sigfox instead of Wi-Fi because I wanted to use a battery pack. If you don’t want to use battery pack then I think Wi-Fi would be more suitable as it is easier and more familiar to connect.

The device is placed near the window as to get the best connection and correct result from light outdoors. I have also connected a battery pack to it which is why I decided to use Sigfox instead of Wi-Fi.

The configuration that is stored on the pycom device is used to connect to my nearest Sigfox antenna and the code in pybytesclient will open that file and use the credentials stored there to connect to Sigfox and transmit the data to the pybytes service.

If you want to do the same as I did with Sigfox then I would recommend to follow this [guide](https://hackmd.io/@lnu-iot/SyUxJU7pu) on how to connect Sigfox with the lopy4 device. Sigfox may not be available everywhere, if thats the case then I would recommend to just use WiFi.

The code in the pybytes client is using MQTT as a transfer protocol and it will transmit sensordata once every 15 minutes. 

### [ ](https://hackmd.io/@lnu-iot/iot-tutorial#Presenting-the-data "Presenting-the-data")Presenting the data

In Pybytes you can create different types of dashboards, it is easy to set it up.
For instructions on how to setup you can find [here](https://docs.pycom.io/pybytes/dashboard/)

Here is how my dashboard looks. The spikes on the charts tells that during that time it was the brightest in our balcony which is around 17.00 because the sun during that time shines directly at the photoresistors.
![](https://i.imgur.com/D5p4W3x.png)

Unfortunately Pybytes can only save data for 1 month, everything older than that will be deleted so if you want to store data on a longer time period then I would recommend to use a paid subscription on another platform, one that I can recommend is called[Datacake](https://datacake.co/) which can retain data for up to one year for a reasonable subscription fee.

### [ ](https://hackmd.io/@lnu-iot/iot-tutorial#Finalizing-the-design "Finalizing-the-design")Finalizing the design

I think the project was very interesting and fun. It gave me the opportunity to learn some simple electronics and basic Python programming.

Here is how my project looks like.
![](https://i.imgur.com/RN4ALRu.jpg)

Conclusions that I can draw from this project is that I get sunshine in the window around 17.00 and then it will just be less and less light for the rest of the day and the sun will go up at 3.20 in the morning.

This will be different if placed somewhere else or in another apartment.
Unfortunately you cannot use this to measure when the sun actually will set by just placing it near a window, you may have to place it somewhere else like on a roof to get a better result on when the sun sets.

Obviously, the sun will go up later in the morning and set earlier than 17.00 as the days are now getting shorter and it would be cool to see that data, but the course only lasts this summer and I only have data older than one month right now.

Some suggestions for improvement could be getting a larger battery pack if you want it to last longer without replacing new batteries every month, it would be cool to attach an OLED display on a secondary breadboard that can show the current temperature and humidity. Another good suggestion for improvement would be to install an  [airquality sensor](https://www.electrokit.com/produkt/miljosensor-scd-30-co2-temperatur-rh/) which measures CO2 concentration in the air.
It would be also good to send to pybytes on how much battery power is left. I also wish I could store the data on another platform for example datacake as mentioned above, which can save data for up to one year.

##### Footnotes
[1] [Wireless technologies in IoT, Marco Zennaro](https://www.youtube.com/watch?v=oer414snO0o&list=PL70wNv4dBdJzuVMTC3OL6YPnENS8Y7TKn)
[2] [Humidity on Wikipedia](https://en.wikipedia.org/wiki/Humidity)



