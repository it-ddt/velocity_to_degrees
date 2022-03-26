degrees_guess = {
    0: (0, -10),
    22.5: (5, -15),
    45: (10, -10),
    67.5: (15, -5),
    90: (10, 0),
    112.5: (15, 5),
    135: (10, 10),
    157.5: (5, 15),
    180: (0, 10),
    202.5: (-5, 15),
    225: (-10, 10),
    247.5: (-15, 5),
    270: (-10, 0),
    292.5: (-15, -5),
    315: (-10, -10),
    337.5: (-5, -15)
}

import math

def degrees_to_velocity(degrees) -> tuple:
    speed = 10
    radians = math.radians(degrees)
    velocity_x = (math.sin(radians) * speed)
    velocity_y = (math.cos(radians) * speed)
    velocity_x = math.floor(velocity_x)
    velocity_y = math.floor(velocity_y) * -1  # в pygame y растет вниз
    return(velocity_x, velocity_y)


if __name__ == "__main__":
    angles = (
        0,
        22.5,
        45,
        67.5,
        90,
        112.5,
        135,
        157.5,
        180,
        202.5,
        225,
        247.5,
        270,
        292,
        315,
        337.5
    )

    for angle in angles:
        print(angle, degrees_to_velocity(angle))