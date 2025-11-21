import numpy as np
import matplotlib.pyplot as plt

voltages = np.load("voltages.npy")
spikes = np.load("spikes.npy")

t = range(len(voltages))

fig, ax1 = plt.subplots(figsize=(12, 5))

ax1.plot(t, voltages, linewidth=1.2)
ax1.set_xlabel("Time")
ax1.set_ylabel("Membrane Potential (mV)")

ax2 = ax1.twinx()
ax2.plot(t, spikes, linestyle="None", marker="|", markersize=8)
ax2.set_ylabel("Spikes")

plt.tight_layout()
plt.show()
