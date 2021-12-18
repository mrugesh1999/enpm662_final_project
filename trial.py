import math
import numpy
from matplotlib import pyplot as plt
import header

d = 0.5  # in m

path_travelled = [(0.5, 2), (0.75, 0.45), (1.25, 1.3)]
solutionla_t1 = []
solutionla_t2 = []
solutione_theta = []
path_travelled = header.reach((0, -0.1), (0, 0.5), 0.6)
shoulder_path = header.shoulder_reach((0, 0.6), (0, 0), 0.6)
getting_it_down_path = header.reach((0, 0), (0, 0.6), 0.6)
path_next = path_travelled


for each in path_next:
    temp_solutionla_t1, temp_solutionla_t2 = header.arm_transforming(each[0], each[1], d)
    solutionla_t1.append(temp_solutionla_t1)
    solutionla_t2.append(temp_solutionla_t2)
    solutione_theta.append(header.shoulder_transforming(0, -0.6))
direction_change = len(solutionla_t2)
for each in shoulder_path:
    temp = header.shoulder_transforming(each[0], each[1])
    solutione_theta.append(temp)
    solutionla_t1.append(solutionla_t1[-1])
    solutionla_t2.append(solutionla_t2[-1])

getting_it_down_path =sorted(getting_it_down_path, reverse=True)
for each in getting_it_down_path:
    temp_solutionla_t1, temp_solutionla_t2 = header.arm_transforming(each[0], each[1], d)
    solutione_theta.append(solutione_theta[-1])
    solutionla_t1.append(temp_solutionla_t1)
    solutionla_t2.append(temp_solutionla_t2)


solutionarm_torque1 = []
solutionarm_torque2 = []
counter = 0
for each in solutione_theta:
    counter = counter + 1
    if counter < direction_change + 1:
        solutionarm_torque1.append(0)
    else:
        solutionarm_torque1.append(header.torque_arm1(each))

for each in solutionla_t1:
    solutionarm_torque2.append(header.torque_arm2(each))


x = range(len(solutionla_t2))

plt.scatter(x, solutionla_t1, color = 'hotpink')
plt.scatter(x, solutionla_t2, color = '#88c999')
plt.scatter(x, solutione_theta, color = '#ffa859')
plt.legend(['Arm θ 1' , 'Arm θ 2', 'Elbow θ'])
plt.show()
plt.scatter(x, solutionarm_torque1, marker='o', color = 'hotpink')
plt.scatter(x, solutionarm_torque2, marker='^', color = '#69c420')
plt.legend(['Shoulder Trq', 'Elbow Trq'])
plt.show()