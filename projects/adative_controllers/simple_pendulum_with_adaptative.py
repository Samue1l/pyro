# -*- coding: utf-8 -*-
"""
Created on 19/11/2019

@author: Pierre
"""
###############################################################################
import numpy as np
###############################################################################
from pyro.dynamic import pendulum
from adaptive_computed_torque import SinglePendulumAdaptativeController
###############################################################################

sys = pendulum.SinglePendulum()
sys.cost_function = None
ctl = SinglePendulumAdaptativeController( sys )

sys.m1 = 1

#ctl.A[0] = 0
#ctl.A[1] = 0

ctl.z0[0] = 15
ctl.z0[1] = 2

ctl.Kd = 1
ctl.lam = 1
ctl.T[0,0] = 10
ctl.T[1,1] = 10
# Set Point
q_target = np.array([3.14])
ctl.rbar = q_target

# New cl-dynamic
cl_sys = ctl + sys

# Simultation
cl_sys.x0[0]  = 0

cl_sys.compute_trajectory(tf=10, n=20001, solver='euler')
cl_sys.plot_phase_plane_trajectory()
cl_sys.plot_trajectory('xu')
cl_sys.plot_trajectory_with_internal_states()
cl_sys.animate_simulation()