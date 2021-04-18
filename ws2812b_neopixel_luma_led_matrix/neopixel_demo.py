import math
import time
import colorsys

from luma.led_matrix.device import neopixel
from luma.core.render import canvas


class WS2812_Neopixel:
    def __init__(self):
        # create matrix device
        self.device = neopixel(width=24, height=1)
        self.status = True;

    def get_status(self):
        return self.status

    def terminate(self):
        self.status = False

    def wipe(self,ecolor,cycles):
        #colors = [ecolor, ecolor, ecolor, ecolor]
        color = ecolor
        #while True:
        l = 0
        for i in range(cycles):
            for y in range(self.device.height):
                for x in range(self.device.width):
                    with canvas(self.device) as draw:
                        z = y + 1
                        for temp in range(z):
                            if temp + 1 == z:
                                draw.line((0, y, x, y), fill=color)
                            else:
                                draw.line((0, temp, self.device.width, temp), fill=color)

                    if l ==0:
                        time.sleep(0.02)
                        l=1
                    else:
                        time.sleep(0.05)
                        l=0

    def gfx(self, effect, ecolor, cycles):
        effects_dict = {"wipe": self.wipe}

        if effect not in effects_dict.keys():
            return

        chosen_effect = effects_dict.get(effect)

        for i in range(1):
            with canvas(self.device) as draw:
                if effect == "wipe":
                    self.wipe(ecolor, cycles)
                else:
                    return

                    #     time.sleep(0.01)

