import network
import ssd1306
from machine import Pin, I2C, ADC
from writeoled import write
from time import sleep
net = network.WLAN(network.STA_IF)

while True:
    write([net.ifconfig()[0]])
    sleep(2)