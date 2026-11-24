from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Color

sensor = ColorSensor(Port.S1)

while True:
    if sensor.color() == Color.RED:
        ev3.speaker.beep(500)
    elif sensor.color() == Color.BLUE:
        ev3.speaker.beep(1000)
