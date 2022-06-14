from machine import Pin

# This is for turning off the led indicator on the expansion board

led = Pin('P9', mode = Pin.OUT)
button = Pin('P10', mode = Pin.IN)
led.value(1)
