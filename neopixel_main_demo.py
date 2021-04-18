import argparse
from ws2812b_neopixel_luma_led_matrix.neopixel_demo import WS2812_Neopixel

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Input effects for ws2812b/neopixel")
    parser.add_argument('effect', type=str, help="Input Effect Type")
    parser.add_argument('ecolor', type=str, help="Input Color")
    parser.add_argument('cycles', type=int, help="Input number of Cycles")
    args = parser.parse_args()
    print(f"Received command line effect argument : {args.effect} {args.ecolor} {args.cycles}")

    try:
        #while True:
        neo_pixel = WS2812_Neopixel()
        neo_pixel.gfx(args.effect, args.ecolor, args.cycles)
        print("Main Loop")
    except KeyboardInterrupt:
        pass
    except:
        pass


