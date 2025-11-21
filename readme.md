This project simulates an advanced Leaky Integrate-and-Fire (LIF) neuron.

<img width="850" height="347" alt="image" src="https://github.com/user-attachments/assets/7f4a0bc2-7e7a-40b4-acd3-f449e949cc16" />

- Image credits: Research Gate


Attributes:
- Realistic membrane potential accumulation
- Threshold-based spiking at -55 mV
- Reset dynamics after firing
- Refractory period during which no new spikes can occur
- Passive leak towards the resting potential (-70 mV)

Files:  
- lif.py : main simulation
- visualization.py : the script for creating the graph of simulation.
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

Ouput of the visualization.py file:
<img width="1490" height="698" alt="image" src="https://github.com/user-attachments/assets/5de986c6-d16a-4235-8e85-76290ca27a0e" />


