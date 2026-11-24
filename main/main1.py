from pybricks.hubs import EV3Brick
from pybricks.parameters  import Button, Color
from pybricks.tools import wait

ev3 = EV3Brick()
ev3.scree.print("Hallo, EV3!")

while True:
    tasten = ev3.buttons.pressed()
    if Button.Left in tasten:
        ev3.light.on(Color.GREEN)
    else:
        ev3.light.off()
    if Button.CENTER in tasten:
        ev3.speaker.beep()
        wait(300)
    wait(50)