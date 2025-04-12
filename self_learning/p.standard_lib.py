import pandapower as pp
import pandas as pd

# Mejorar la visualización de datos
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', None)

net = pp.create_empty_network()
print(pp.available_std_types(net, element="line"))

b1 = pp.create_bus(net, vn_kv=.4)
b2 = pp.create_bus(net, vn_kv=.4)
lid = pp.create_line(net, from_bus=b1, to_bus=b2, length_km=0.1, std_type="NAYY 4x50 SE", name="test_line")
print(net.line.loc[lid])

