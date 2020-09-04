import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import time
import math


plt.style.use('ggplot')

current_array = []
func_array = []
start_time = time.time()
while True:
    current_time = time.time() - start_time
    t = 5 * math.sin ( 2 * math.pi * 1 * current_time )
    func = 3 * math.pi * math.exp(-t) 
    current_array.append(current_time)
    func_array.append(func)
    print(current_time)
    if(len(current_array)>20):
        current_array.pop(0)
        func_array.pop(0)
    plt.cla()
    plt.plot(current_array,func_array)
    plt.xlabel ('Time')
    plt.ylabel ('h ( t )')
    plt.title ('h ( t ) = 3 * pi * exp(-lambda [ t ] )')
    plt.grid()
    plt.pause(0.01)

plt.show()