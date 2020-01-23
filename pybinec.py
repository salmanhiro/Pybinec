# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 13:36:24 2019

@author: SAF

Pybinec is a eclipsing binary simulation, but not very ideal
"""

def radius_ratio(p_h,c_ecl,t_ecl):
    import numpy as np
    AB = 0.5*(c_ecl - t_ecl)
    theta = AB*2*(np.pi)/p_h
    d_theta = t_ecl*2*(np.pi)/p_h
    R1_R2 = (theta + d_theta)/theta
    if R1_R2 <= 0 :
        return "take a rest, you are drunk"
    else: 
        return R1_R2

def dist_from_cmass(vr,p,incline): #Distance from center of mass
    import numpy as np
    r = vr*p/((2*np.pi)*np.sin(np.deg2rad(incline)))
    return r #for each star varies from radial velocity, period and inclination

def m_to_au(dist):
    from astropy import units as u
    x = dist * u.meter
    return x.to(u.au).value

def stellar_radius(theta,dist, R1_R2):
    from astropy import units as u
    x = dist * u.au
    R2 = (theta*dist)/2
    R1 = R1_R2*R2
    return [R1,R2]

def kepler(a,per):
    m1_plus_m2 =((4*(np.pi)**2)/6.67408e-11)*((a**3)/(per**2))
    return m1_plus_m2

def mass_ratio(vr1,vr2):
    m1_m2 = vr2/vr1
    return m1_m2

def mass(vr1,vr2,mass_total, mass_ratio):
    m2 = total_mass/((vr2/vr1)+1)
    m1 = mass_ratio*m2
    return [m1,m2]


