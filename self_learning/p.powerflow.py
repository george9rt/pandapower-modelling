#import packages
import pandapower as pp
import pandapower.networks
import pandas as pd

# Mejorar la visualización de datos
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 200)
pd.set_option('display.max_colwidth', None)

net = pandapower.networks.example_simple()
print(net)

#Run power flow and acces results 
pp.runpp(net)
print(net)
print(net.res_bus)

#min and max voltage in the minimum voltage level
print(net.res_bus[net.bus.vn_kv==20.].vm_pu.min())
load_or_generation_buses = set(net.load.bus.values) | set(net.sgen.bus.values) | set(net.gen.bus.values)
print(net.res_bus.vm_pu.loc[list(load_or_generation_buses)].max())

#Results Table
print(net.res_bus)
print(net.res_ext_grid)
print(net.res_line)
print(net.res_trafo)
print(net.res_load)
print(net.res_sgen)
print(net.res_gen)
print(net.res_shunt)

#Voltage Angles and Initialization Calculation
print(net.ext_grid.va_degree)
print(net.trafo.shift_degree)
pp.runpp(net)
print(net.res_bus.va_degree)

#Radial vs Mesh network ---> Radial network I can associate with an unifilar diagram
pp.runpp(net,calculate_voltage_angles=True)
pp.runpp(net, calculate_voltage_angles=True, init="dc")
print(net.res_bus.va_degree)

#Transformer Model ---> T model
pp.runpp(net,trafo_model="t")
print(net.res_trafo)

#Transformer Model ---> pi model
pp.runpp(net,trafo_model="pi")
print(net.res_trafo)

#Transformer Loading
pp.runpp(net,trafo_loading="current")
print(net.res_trafo)
pp.runpp(net,trafo_loading="power")
print(net.res_trafo)

#Generator Reactive Power Limits
print(net.gen) #the generator has reactive power limits: +-3 Mvar
pp.runpp(net)
print(net.res_gen)
pp.runpp(net, enforce_q_lims=True)
print(net.res_gen)

#setting user options
pp.runpp(net)
net.res_bus

pp.set_user_pf_options(net, calculate_voltage_angles=True, init="dc")
pp.runpp(net)
print(net.res_bus)

pp.runpp(net, calculate_voltage_angles=False)
print(net.res_bus)