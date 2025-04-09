#import initial commands 
import pandas as pd
import pandapower as pp
import pandapower.networks as nw

# Show all rows and columns 
pd.set_option('display.max_rows', 20)  
pd.set_option('display.max_columns', 50) 

net = nw.simple_four_bus_system()
print(net) #It shows the number of elements of the network
print(net.bus) # It includes the specific information of the buses

pp.runpp(net) 
print(net)

print(net.res_bus)

print(net.line)
print(net.res_line)

