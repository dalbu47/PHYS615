import numpy as np

g = 1
theta = (np.pi) / 4
thetalist = [0.4, 0.5, 0.6, 0.7, 0.8]
thetalist2 = [0.621, 0.622, 0.623]
Vter = 1
Vo = 1
Vxo = 1 / (np.sqrt(2))
Vyo = 1 / (np.sqrt(2))

Rvac = (2 * Vxo * Vyo) / g
Rlist = []
dlist = []
R = np.linspace(0, 0.65, 10000)


for i in range(len(R)):
    y = ((Vyo + Vter) / Vxo) * R[i] + (Vter ** 2) * np.log(1 - (R[i] / (Vxo * Vter)))
    Rlist.append(y)

d = R[np.where(np.diff(np.sign(Rlist)))[0][1]]
print(f"For the angle 45 degrees, the Range in a vacuum Rvac is {Rvac:0.3f}m, and {d:0.3f}m is the Range R in a linear medium.")


for j in range(len(thetalist)):
    Rlist = []
    for i in range(len(R)):
        Vx = np.cos(thetalist[j])
        Vy = np.sin(thetalist[j])
        y = ((Vy + Vter) / Vx) * R[i] + np.log(1 - (R[i] / Vx))
        Rlist.append(y)
    d = R[np.where(np.diff(np.sign(Rlist)))[0][1]]
    dlist.append(d)

print(f"For the angles 0.4, 0.5, 0.6, 0.7 and 0.8 radians, the ranges in a linear medium are {dlist[0]:0.3f}, {dlist[1]:0.3f}, {dlist[2]:0.3f}, {dlist[3]:0.3f}, and {dlist[4]:0.3f} meters respectively.")
dlist2 = []
for j in range(len(thetalist2)):
    Rlist2 = []
    for i in range(len(R)):
        Vx = np.cos(thetalist2[j])
        Vy = np.sin(thetalist2[j])
        y = ((Vy + Vter) / Vx) * R[i] + np.log(1 - (R[i] / Vx))
        Rlist2.append(y)
    d = R[np.where(np.diff(np.sign(Rlist2)))[0][1]]
    dlist2.append(d)
print(f"After some trial and error, I found that the maximum range is {dlist2[1]:0.3f} meters which happens at {thetalist2[1]:} radians.\nCompared to the value in a vacuum for 45 degrees calculated earlier, it is about half as large.")

#%%
