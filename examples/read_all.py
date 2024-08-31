"""Show the value of all known registers."""
from sun2000_modbus.inverter import Sun2000
from sun2000_modbus.registers import InverterEquipmentRegister, BatteryEquipmentRegister, MeterEquipmentRegister

inverter = Sun2000('192.168.179.3')
inverter.connect()

print('\nInverter\n=====================')
for register in InverterEquipmentRegister:
    value = inverter.read_formatted(register)
    print(f'{register.name}: {value}')

print('\nBattery\n=====================')
for register in BatteryEquipmentRegister:
    value = inverter.read_formatted(register)
    print(f'{register.name}: {value}')

print('\nMeter\n=====================')
for register in MeterEquipmentRegister:
    value = inverter.read_formatted(register)
    print(f'{register.name}: {value}')
