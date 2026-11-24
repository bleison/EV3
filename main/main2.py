from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port, Color

left = Motor(Port.B)
right = Motor(Port.C)
sensor = TouchSensor(Port.S1)

while True:
    if sensor.presses():
        left.stop()
        right.stop()
    else:
        left.run(500)
        right.run(500)