import numpy as np
import matplotlib.pyplot as plt
import math as m

# Circuit parameters
R = 24.5   # Resistance in ohms
C = 460e-12   # Capacitance in farads
L = 2.2e-3   # Inductance in henries
Vc0 = 5           # Initial capacitor voltage

a = R/L
b = 1/(L*C)
disc = (a*a/4) - b

# Simulation parameters
stepsize = 1e-9
tmax = 2e-4    # Maximum simulation time

size = int(tmax / stepsize)

t = np.linspace(0, tmax, size)

if disc < 0:
    w = np.sqrt(-disc)
    Vc = Vc0*(np.exp(-a*t/2))*(np.cos(w*t) + (a/(2*w))*(np.sin(w*t)))
elif m.fabs(disc) <= 1e-5:
    Vc = Vc0*(1+a*t/2)*(np.e**(-a*t/2))
elif disc > 0:
    w = np.sqrt(disc)
    s1 = -a/2 + w
    s2 = -a/2 - w
    A = Vc0 * s2 / (s2 - s1)
    B = Vc0 * s1 / (s1 - s2)
    Vc = A * np.e**(s1 * t) + B * np.e**(s2 * t)

# Plot results
plt.plot(t, Vc)
plt.savefig("../figs/rlc.png")
plt.xlabel("Time (s)")
plt.ylabel("Voltage across capacitor (Vc)")
plt.title("Current vs. Time in an RLC Circuit")
plt.show()

