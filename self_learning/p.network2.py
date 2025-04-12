import pandapower as pp
import pandas as pd

# Mejorar la visualización de datos
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 200)
pd.set_option('display.max_colwidth', None)

net = pp.create_empty_network() #create empty network

#Buses
bus1= pp.create_bus(net, vn_kv=110, name="HV Busbar", type="b")
bus2= pp.create_bus(net, vn_kv=110, name="HV Busbar 2", type="b")
bus3= pp.create_bus(net, vn_kv=110, name="HV Transformer Bus", type="n")
bus4= pp.create_bus(net, vn_kv=20, name="MV Transformer Bus", type="n")
bus5= pp.create_bus(net, vn_kv=20, name="MV Main Bus", type="b")
bus6= pp.create_bus(net, vn_kv=20, name="MV Bus 1", type="b")
bus7= pp.create_bus(net, vn_kv=20, name="MV Bus 2", type="b")

print(net.bus)
print(bus6)

#External Grid
pp.create_ext_grid(net, bus=bus1, vm_pu=1.02, va_degree=40 )
print(net.ext_grid)

#Transformer
print(pp.available_std_types(net, element="trafo"))
trafo1=pp.create_transformer(net,hv_bus=bus3,lv_bus=bus4,name="110/20kV transformer",std_type="25 MVA 110/20 kV")   
print(net.trafo)

#Line 
line1=pp.create_line(net,bus1,bus2,length_km=10,std_type="N2XS(FL)2Y 1x300 RM/35 64/110 kV",  name="Line 1")
line2=pp.create_line(net,bus5,bus6,length_km=2,std_type="NA2XS2Y 1x240 RM/25 12/20 kV", name="Line 2")
line3=pp.create_line(net,bus6,bus7,length_km=3.5,std_type="48-AL1/8-ST1A 20.0", name="Line 3")
line4=pp.create_line(net,bus5,bus7,length_km=2.5,std_type="NA2XS2Y 1x240 RM/25 12/20 kV", name="Line 4")
print(net.line)

#Switches
sw1=pp.create_switch(net,bus2,bus3,et="b",type="CB",closed=True)
sw2=pp.create_switch(net,bus4,bus5,et="b",type="CB",closed=True)

sw3=pp.create_switch(net,bus5,line2,et="l",type="LBS",closed=True)
sw4=pp.create_switch(net,bus6,line2,et="l",type="LBS",closed=True)
sw5=pp.create_switch(net,bus6,line3,et="l",type="LBS",closed=True)
sw6=pp.create_switch(net,bus7,line3,et="l",type="LBS",closed=False)
sw7=pp.create_switch(net,bus7,line4,et="l",type="LBS",closed=True)
sw8=pp.create_switch(net,bus5,line4,et="l",type="LBS",closed=True)
print(net.switch)

#Load
pp.create_load(net,bus7,p_mw=2,q_mvar=4,scaling=0.6,name="Load")
print(net.load)
#voltage dependent loads
#ZIP load model, which allows a load definition as a composition of constant power, constant current and constant impedance.
pp.create_load(net,bus7,p_mw=2,q_mvar=2,const_z_percent=30,const_i_percent=20,name="ZIP Load")
print(net.load)

#Static Generator
pp.create_sgen(net,bus7,p_mw=2,q_mvar=-0.5,name="Static Generator")
print(net.sgen)

#Shunt
pp.create_shunt(net,bus3,q_mvar=-0.96,p_mw=0,name="Shunt")
print(net.shunt)

