# -*- coding: utf-8 -*-
"""
Created on March 20 2020

@author: Pierre
"""
###############################################################################
import numpy as np
import math
###############################################################################
from wcrt import WCRT 
from projects.adative_controllers import adaptive_computed_torque

###############################################################################

pi = math.pi

sys = WCRT()
sys.cost_function = None
ctl  = adaptive_computed_torque.AdaptativeController_WCRT( sys )

#Param Wcrt
sys.d1 = 3
sys.d2 = 2
sys.d3 = 2

sys.k1 = 10
sys.k2 = 10
sys.k3 = 10

sys.m1 = 2
sys.m2 = 1
sys.m3 = 1

sys.l1  = 0.5 
sys.l2  = 0.8
sys.l3  = 0.8
sys.lc1 = 0.4
sys.lc2 = 0.5
sys.lc3 = 0.7

#Param adapt-control
ctl.A[0] = 5
ctl.A[1] = 5
ctl.A[2] = 5
ctl.A[3] = 0
ctl.A[4] = 5
ctl.A[5] = 20
ctl.A[6] = 10
ctl.A[7] = 0

ctl.Kd[0,0] = 7
ctl.Kd[1,1] = 7
ctl.Kd[2,2] = 7

ctl.lam = 1.5

ctl.T[0,0] = 8
ctl.T[1,1] = 8
ctl.T[2,2] = 8
ctl.T[3,3] = 8
ctl.T[4,4] = 8
ctl.T[5,5] = 8
ctl.T[6,6] = 8
ctl.T[7,7] = 8

# Set Point
ctl.rbar = np.array([0,0,0])

# New cl-dynamic
cl_sys = ctl + sys
#cl_sys = sys

# Simultation
cl_sys.x0[0]  = pi/3
cl_sys.x0[1]  = 1
cl_sys.x0[2]  = 0

cl_sys.compute_trajectory(tf=10, n=20001, solver='euler')
cl_sys.plot_trajectory()
#cl_sys.plot_trajectory_with_internal_states()
cl_sys.animate_simulation(is_3d = True)

