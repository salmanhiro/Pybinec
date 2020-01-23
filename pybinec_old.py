"""
Created on Fri Sep  6 22:25:20 2019
@author: hiro
"""

import numpy as np
import pandas as pd

print("This is Pybinec, an Eclipsing Binary Star Determiner")
print("\n")
print("   A           D             E         H    ")
print("----           ---------------         -----")
print("    \         /               \       /     ")
print("     \       /                 \_____/      ")
print("      \     /                  F     G      ")
print("     B \___/ C                              ")
print("\n")

print("We will determine: ")
print("1. Stars Radius")
print("2. Stars Mass")
print("3. Stars Temperature Ratio")


period = float(input("enter star period in days: "))
c_ecl = float(input("enter eclipse contact time (A-D) in hours: "))
t_ecl = float(input("enter total eclipse time (B-C) in hours: "))
    
AB = 0.5*(c_ecl - t_ecl)
p_s = period*24*3600
p_h = period*24
theta = AB*2*(np.pi)/p_h
d_theta = t_ecl*2*(np.pi)/p_h
    
R1_R2 = (theta + d_theta)/theta
if R1_R2 <= 0 :
    print("\n take a rest mate, u r drunk")
else:
    print("\n R1/R2 = ", R1_R2)
    
vr_1 = float(input("enter radial velocity amplitude for star 1: "))
vr_2 = float(input("enter radial velocity amplitude for star 2: "))
inc = float(input("enter inclination (deg): "))
        
def radius(vr,p,incline):
    r = vr*p/((2*np.pi)*np.sin(np.deg2rad(incline)))
    return r
        
def m_to_au(dist):
    return dist*6.68459e-12
        
r_1 = radius(vr_1,p_s,inc)
r_2 = radius(vr_2,p_s,inc)

print("r1 = ",r_1,"          m  ","  r2 = ",r_2, " m ") 
print("r1 = ",m_to_au(r_1)," au  "," r2 = ",m_to_au(r_2), " au ") 
r = r_1+r_2
R_2 = (theta*r)/2
R_1 = R1_R2*R_2
print("R1 = ",R_1,"          m  ","  R2 = ",R_2, " m ") 
        
mag_normal = float(input("enter non eclipsing magnitude: "))
mag_eclipsing_p = float(input("enter primary eclipse magnitude: "))
mag_eclipsing_s = float(input("enter secondary eclipse magnitude: "))


def kepler(a,per):
    m1_plus_m2 =((4*(np.pi)**2)/6.67408e-11)*((a**3)/(per**2))
    return m1_plus_m2

total_mass = kepler(r,p_s)
m1_m2 = vr_2/vr_1
print("m1 + m2: ", total_mass)
print("m1/m2: ", m1_m2)

def m2(vr2,vr1,mass):
        m_2 = mass/((vr2/vr1)+1)
        return m_2
    
m_s2 = m2(vr_2,vr_1,total_mass)

print("Mass of star 2: ", m_s2)
    
m_s1 = m1_m2*m_s2

print("Mass of star 1: ",m_s1)

data = [['1', R_1, r_1, m_s1, vr_1, period], 
        ['2', R_2, r_2, m_s2, vr_2, period]] 
save_session = pd.DataFrame(data, columns = ['obj', 'R(m)', 'r(m)','v_rmax(m/s)', 'm(kg)',
                                             'p(day)'])
save_session.to_csv("bin_kine.csv")