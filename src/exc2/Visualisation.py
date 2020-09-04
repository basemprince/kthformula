import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import time
import math

#plt.style.use('fivethirtyeight')
plt.style.use('ggplot')

current_array = []
func_array = []

while True:
    current_time = time.time()
    t = 5 * math.sin ( 2 * math.pi * 1 * current_time )
    func = 3 * math.pi * math.exp(-t) 
    current_array.append(current_time)
    func_array.append(func)

    if(len(current_array)>20):
        current_array.pop(0)
        func_array.pop(0)
    plt.cla()
    plt.plot(current_array,func_array)
    plt.pause(0.01)
    
    plt.xlabel ('Time')
    plt.ylabel ('Function')
    plt.title ('h ( t ) = 3 * pi * exp(-lambda [ t ] )')
    plt.grid()
    
plt.show()




# plt.axis([0, 10, 0, 1])

# for i in range(10):
#     y = np.random.random()
#     plt.scatter(i, y)
#     plt.pause(0.05)

# plt.show()