from machine import Pin, I2C
import ssd1306

def write(list):
    line = 0
    i2c = I2C(scl=Pin(5), sda=Pin(4))
    oled_width = 64
    oled_height = 48
    oled = ssd1306.SSD1306_I2C(oled_width,oled_height,i2c)
    for item in list:
        oled.text(item,0,line)
        line+=10
    oled.show()
