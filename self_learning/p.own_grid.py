#import commands
import pandas as pd
import pandapower as pp 
import pandapower.topology as top

# Show all rows and columns 
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#create empty network
net = pp.create_empty_network()

#create bus function
b1 = pp.create_bus(net, vn_kv=20., name="Bus 1")
b2 = pp.create_bus(net, vn_kv=0.4, name="Bus 2")
b3 = pp.create_bus(net, vn_kv=0.4, name="Bus 3")    

#Load
    #Active Power: 100kW
    #Reactive Power: 50 kVar

#create elements 
pp.create_ext_grid(net, bus=b1, vm_pu=1.02, name="Grid Connection")
pp.create_load(net, bus =b3, p_mw=0.1, q_mvar=0.05, name="Load")

#create branch elements
print(pp.available_std_types(net, element="trafo"))
print(pp.available_std_types(net, element="line"))
#We have to previous select both types to understand which of these branch elements we will use
trafo=pp.create_transformer(net, hv_bus=b1, lv_bus=b2, std_type="0.4 MVA 20/0.4 kV", name="Trafo")
line=pp.create_line(net, from_bus=b2, to_bus=b3, length_km=0.1, std_type="NAYY 4x50 SE", name="Line")

#Data Structure 
    #Each dataframe in a pandapower net object contains the information about one pandapower element,
    #such as line, load, transformer,etc
print(net.bus)
print(net.line)
print(net.trafo) 
print(net.load)

#Power Flow
#Now we run a power flow:
pp.runpp(net)

#And check out at the results for buses, lines and transformers 
print(net.res_bus)
print(net.res_line)
print(net.res_trafo)

#Tap Changers
    #We now lower the tap changer position, from position 0 to -1 and run another power flow
net.trafo.tap_pos.at[trafo]=-1
pp.runpp(net)

#Looking at the results shows that bus voltages at the low voltage side of the transformer have increased
print(net.res_bus)

#Switches 
    #We now create an open switch at the load bus:
pp.create_switch(net, bus=b3, element=line, et="l", closed=False)

#The open switch cuts the load bus from power supply
    #This can be verified by running a power flow and inspecting the results.
    # The voltage at bus 2 is given as NAN
pp.runpp(net)
net.res_bus
print(net.res_load)

#And the line is in open loop operation:
print(net.res_line) #The behaviour is in loop due to the closed switch


#Topological Analysis 
top.unsupplied_buses(net)


net.switch.closed.at[0]=True
top.unsupplied_buses(net)

mg=top.create_nxgraph(net,include_trafos=False)






