import time
import pycom
import machine
from machine import I2C
from machine import Pin

from _pybytes import Pybytes
from _pybytes_config import PybytesConfig


conf = PybytesConfig().read_config()

pybytes = Pybytes(conf)

pybytes.start()
pybytes.send_ping_message()


def sendData(arrData):
    n = 1
    
    for data in arrData:
        pybytes.send_signal(n,data)
        n += 1
    
