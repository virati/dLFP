#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 18:07:46 2019

@author: virati
Splitting our simulation of the dLFP into separate script
"""

import DBSpace.dLFP.diff_model as diff_model
from DBSpace.dLFP.diff_model import sim_diff, sim_amp

print('dLFP Simulation for Mismatch Compression - Script')
diff_run = sim_diff(Ad=500,wform='moresine4',clock=True,stim_v=6)
#diff_run.set_brain()
#diff_run.set_stim(wform='ipg')

amp_run = sim_amp(diff_run,family='tanh',noise=1e-6,sig_amp_gain=1,pre_amp_gain=1)

#diff_run.plot_V_out(1000,1200)
#diff_out = diff_run.V_out(1000,1100)['sim_1']
Z1 = 1200
Z3 = 1300

amp_run.simulate(Z1,Z3)
amp_run.plot_time_dom()
amp_run.plot_freq_dom()
amp_run.plot_tf_dom()