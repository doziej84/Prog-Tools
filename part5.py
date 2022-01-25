# -*- coding: utf-8 -*-
"""
Part 5 : Vertical trajectory
"""
import numpy as np
import matplotlib.pyplot as plt

##............Height function
def get_height (t, g, v0):
    return v0*t - 0.5 *g *t**2

##...Parameters
tmin,tmax = 0, 2
Niter =20
v0=5 # velocity
g=9.81 # m/s**2


#..........Time steps
step = (tmax - tmin)/ Niter

t = tmin
y_old = 0


# Loop of Niter
for i in range(Niter):
    y_new = get_height(t, g, v0)
    #print(i, y_old, y_new, t)
    #check if y_new < y_old -> reached the peak
    #...conditional statement
    if y_new < y_old:
        print('peak Height: %.2f, at time: %.2f' % (y_old, t))
        t_at_peak = t- step
        y_at_peak = y_old
        #break
     
        
    #update time and height variables 
    t += step
    y_old =y_new
    
    
# create plots
a_t = np.linspace(tmin,tmax-step, Niter)

plt.figure(1)
plt.plot(a_t, get_height(a_t, g, v0))
plt.plot([t_at_peak], [y_at_peak], 'r*')
plt.xlabel( 'Time (s)')
plt.ylabel('Height(m)')
plt.show()





    


