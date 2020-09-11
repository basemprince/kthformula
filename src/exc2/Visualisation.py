import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import time
import math
plt.style.use('ggplot')

# arrays to accumulate time and function results
current_array = []
func_array = []
displayed_data = 20

# the time when the script started
start_time = time.time()
# signal to terminate the script if the plot was closed
go_signal = True

while True and go_signal:
    current_time = time.time() - start_time
    t = 5 * math.sin ( 2 * math.pi * 1 * current_time )
    func = 3 * math.pi * math.exp(-t) 
    current_array.append(current_time)
    func_array.append(func)
    # get rid of the oldest data points after accumulating the allowed displayed_data
    if(len(current_array)>=displayed_data):
        current_array.pop(0)
        func_array.pop(0)
    plt.cla()
    plt.plot(current_array,func_array)
    plt.xlabel ('Time')
    plt.ylabel ('h ( t )')
    plt.title ('h ( t ) = 3 * pi * exp(-lambda [ t ] )')
    plt.pause(0.01)
    go_signal = plt.get_fignums()

plt.show()