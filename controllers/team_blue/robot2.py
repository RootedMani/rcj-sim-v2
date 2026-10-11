from utils import *

def loop(rcj):
    ball_pos = rcj.get_ball_position()
    robot_heading = rcj.get_heading()
    robot_pos = rcj.get_position()
    ball_in_kicker = rcj.is_ball_touched()

    if ball_in_kicker:
        rcj.kick()
    if ball_pos:
        ball_angle = getAngle(rcj, ball_pos)
        moveAngle(rcj, ball_angle, 10, robot_heading)
    else:
        rcj.motor(0, 0, 0, 0)
