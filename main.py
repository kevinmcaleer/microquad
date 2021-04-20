from microbit import *

start = 0x07
end = 0x70

while True:    
    basic.show_arrow(ArrowNames.NORTH)
    if input.button_is_pressed(Button.A):
        basic.show_icon(IconNames.HAPPY)
        print("scanning I2C bus...")
        for i in range(start, end + 1):
            try:
                microbit.i2c.read(i,1)
            except OSError:
                pass
            else:
                print("Found: [%s]" %hex(i))
        print("Scanning complete")



