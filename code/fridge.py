# -*- coding: iso-8859-15 -*-

# Models Newton's Law of Cooling
#    \dfrac{dT}{dt} = -k (T-F)

# The fridge has a constant temperature, F=5 [°C]
# Heat transfer coefficient = k = 0.08       [1/minutes]
#
# Discretizing: T_{i+1} = T_i - k (\delta t)(T_i - F)
#
# Temperature at time point $i+1$ (one step in the future, T_{i+1}) is related
# to the temperature now, at time $i$, T_{i}.

import numpy as np
T_initial = 25     # °C
F_temperature = 5  # °C
delta_t = 0.5      # minutes
time_final = 30
heat_transfer_coeff = 0.08  # 1/minutes

# Create the two outputs of interest
time = np.arange(start=0.0, stop=time_final, step=delta_t)
temp = np.zeros(time.shape)
temp[0] = T_initial

for idx, t_value in enumerate(time[1:]):
    temp[idx + 1] = temp[idx] - heat_transfer_coeff * delta_t * (temp[idx] - F_temperature)

print('{}\n{}'.format(time, temp))
