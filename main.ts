let start = 0x07
let end = 0x70
while (true) {
    basic.showArrow(ArrowNames.North)
    if (input.buttonIsPressed(Button.A)) {
        basic.showIcon(IconNames.Happy)
        console.log("scanning I2C bus...")
    }
    
}
