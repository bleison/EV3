from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor

ev3 = EV3Brick()

medium_motor = Motor(Port.A)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

medium_motor.run_angle()
left_motor.run_angle()
right_motor.run_angle()