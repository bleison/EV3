#!/usr/bin/env pybricks-micropython
# Programm 7: Mit dem Gyrosensor um 90° drehen
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import GyroSensor, Motor
from pybricks.parameters import Port, Direction, Stop
from pybricks.tools import wait

# Initialisierung
ev3 = EV3Brick()

gyro = GyroSensor(
    Port.S2,
    direction=Direction.CLOCKWISE,
)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

gyro.reset_angle(0)

TARGET_ANGLE = 90
SPEED = 100

# Gegenläufige Motoren für eine Drehung nach rechts
left_motor.run(SPEED)
right_motor.run(-SPEED)

# Warten, bis der Zielwinkel erreicht ist
while gyro.angle() < TARGET_ANGLE:
    wait(5)

# Motoren abbremsen
left_motor.stop(Stop.BRAKE)
right_motor.stop(Stop.BRAKE)

# Ergebnis ausgeben
ev3.screen.clear()
ev3.screen.print("Gyro-Winkel: {}°".format(gyro.angle()))
ev3.speaker.beep()