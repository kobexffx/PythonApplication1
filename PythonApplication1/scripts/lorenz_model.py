import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.basemap import Basemap
 
def lorenz_eq(x,y,z,sigma=10.0,rho=28.0,beta=2.667):
    x_out = sigma*(y-x)
    y_out = x*(rho-z)-y
    z_out = x*y - beta*z
    return x_out,y_out,z_out
def run_model(x_i,y_i,z_i,dt,total_step,sigma=10.0,rho=28.,beta=2.667):
    xout = np.zeros(total_step+1)
    yout = np.zeros(total_step+1)
    zout = np.zeros(total_step+1)
    xout[0] = x_i
    yout[0] = y_i
    zout[0] = z_i
    xtemp  = x_i
    ytemp  = y_i
    ztemp  = z_i
    for i in range(total_step):
        xtemp,ytemp,ztemp = lorenz_eq(xout[i],yout[i],zout[i],sigma,rho,beta)
        xout[i+1] = xout[i]+dt*xtemp
        yout[i+1] = yout[i]+dt*ytemp
        zout[i+1] = zout[i]+dt*ztemp
    return xout,yout,zout
xi,yi,zi = np.random.rand(3)
dt = 0.01
total_step = 10000
xs,ys,zs = run_model(xi,yi,zi,dt,total_step)
#####
fig = plt.figure()
ax  = fig.add_subplot(111,projection = '3d')
ax.plot(xs,ys,zs)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.show()



