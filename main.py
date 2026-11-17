#!/usr/bin/env pybricks-micropython
# Programm 3: Mittleren und grossen Motor steuern
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase
from math import pi

# Initialisierung
ev3 = EV3Brick()

medium_motor = Motor(Port.A)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Winkelzähler auf 0 setzen
medium_motor.reset_angle(0)
left_motor.reset_angle(0)
right_motor.reset_angle(0)

# 1. Mittleren Motor um 90° bewegen und zurückfahren
medium_motor.run_target(
    speed=500,
    target_angle=90,
    then=Stop.HOLD,
    wait=True,
)
medium_motor.run_target(
    speed=500,
    target_angle=0,
    then=Stop.COAST,
    wait=True,
)

# 2. DriveBase einrichten und geradeausfahren
wheel_diameter = 56
axle_track = 114
drive_base = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter,
    axle_track,
)

drive_base.straight(500)

# Motorwinkel auslesen
angle_left = left_motor.angle()
angle_right = right_motor.angle()

# Erwartung: 500 mm / (pi * 56 mm) ≈ 2,84 Umdrehungen ≈ 1020°
ev3.screen.print("Links:  {:.0f}°".format(angle_left))
ev3.screen.print("Rechts: {:.0f}°".format(angle_right))

# 3. Auf der Stelle um 90° drehen
drive_base.turn(90)