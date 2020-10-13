import time
import board
import neopixel
import threading
import random
import requests

class LedStrip():
    def __init__(self, pixel_pin=board.D18, num_pixels=60):
        self.pixel_pin = pixel_pin
        self.num_pixels = num_pixels
        self.ORDER = neopixel.GRB
        self.pixels = neopixel.NeoPixel(
                self.pixel_pin,
                self.num_pixels,
                brightness=0.2, 
                auto_write=False,
                pixel_order=self.ORDER
                ) 

    def fadeOut(self):
        for bulb in range(len(self.pixels)):
            self.pixels[bulb] = tuple([max(0, x - 3) for x in self.pixels[bulb]])
            
    def clearPixels(self):
        for bulb in range(len(self.pixels)):
            self.pixels[bulb] = (0, 0, 0)

    def Spell(self, message, delayTime=1):
        prevTime = 0
        lightPtr = 0
        self.active = True
        while self.active:
                self.fadeOut()
                if time.time() - prevTime >= delayTime:
                    prevTime = time.time()
                    self.pixels[lightPtr] = (195, 195, 195)
                    lightPtr += 1 
                    if lightPtr > 5:
                        lightPtr = 0
            self.pixels.show()
            time.sleep(0.001)

if __name__ == '__main__':
    try:
        strip = LedStrip()
        strip.Spell("HELLO")
     
    except KeyboardInterrupt:
        strip.active = False
        strip.clearPixels()
        strip.pixels.show()
