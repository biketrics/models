#                            v_div
#                          +--------+
#                          |        |
#                          v        v
# SENSOR_VOLTAGE ---/\/\/\---/\/\/\--- GND
#                     r1       r2

SENSOR_VOLTAGE = 3.3

r1 = 3000
r2 = 1500

i = SENSOR_VOLTAGE / (r1 + r2)
print(f"Current (A): {i}")

v_div = i * r2
print(f"Divided Voltage (V): {v_div}")