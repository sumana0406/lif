import numpy as np

resting = -70.0
threshold = -55.0
reset_potential = -75.0
leak = 0.1
refractory_period = 5
refractory_timer = 0

v = resting

def lif_step(input_current):
    global v, refractory_timer
    if refractory_timer > 0:
        refractory_timer -= 1
        return 0, v
    v += -leak * (v - resting) + input_current
    if v >= threshold:
        v = reset_potential
        refractory_timer = refractory_period
        return 1, v
    return 0, v

inputs = np.random.normal(1, 5, 1000)
spikes = []
voltages = []

for i in inputs:
    s, v_now = lif_step(i)
    spikes.append(s)
    voltages.append(v_now)

np.save("voltages.npy", np.array(voltages))
np.save("spikes.npy", np.array(spikes))
