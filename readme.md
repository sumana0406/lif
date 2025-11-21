This project simulates an advanced Leaky Integrate-and-Fire (LIF) neuron.

Attributes:
- Realistic membrane potential accumulation
- Threshold-based spiking at -55 mV
- Reset dynamics after firing
- Refractory period during which no new spikes can occur
- Passive leak towards the resting potential (-70 mV)

Files:
- lif_neuron.py : main simulation
- voltages.npy : saved membrane voltage trace
- spikes.npy : saved spike train (1 = spike, 0 = no spike)

To run:
1. Install Python3
2. Install NumPy: pip install numpy
3. Run: python lif_neuron.py

Resulting output:
- Voltage time series stored in voltages.npy
- Spike train stored in spikes.npy

Additional Features:
- Visualize spikes and voltage trace using matplotlib
- Add multiple neurons with synaptic connections
- Add inhibitory neurons
- Add adjustable leak, threshold, or adaptive threshold
