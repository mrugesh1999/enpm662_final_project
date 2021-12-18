import math
import numpy

def arm_transforming(x, z, d):
    left_arm_theta1 = math.atan2(x, z) - math.atan2(math.sqrt(x ** 2 + z ** 2 - d ** 2), d)
    left_arm_theta2 = math.atan2(d ** 2 - (d - z) ** 2, d - z)
    return left_arm_theta1, left_arm_theta2


def shoulder_transforming(x, z):
    shoulder_theta = math.atan2(x, z)
    return shoulder_theta


def reach(initial, final, radius):
    points = []
    intervals = numpy.arange(initial[1], final[1], 1 / 100)
    for each in intervals:
        x = math.sqrt(radius ** 2 - each ** 2)
        points.append((x, each))
    return points


def shoulder_reach(initial, final, radius):
    points = []

    intervals = numpy.arange(final[1], initial[1], 1 / 100)
    for each in intervals:
        x = math.sqrt(radius ** 2 - each ** 2)
        points.append((x, each))
    return points


def torque_arm1(theta):
    return 152.67 * math.cos(theta)


def torque_arm2(theta):
    return 72.82 * math.cos(theta)

