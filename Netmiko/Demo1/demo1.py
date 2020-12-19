from netmiko import ConnectHandler

device = ConnectHandler(device_type='cisco_xe', ip='192.168.122.2', username='cisco', password='cisco')
output = device.send_command('show ip int brief')
print("------------ Output before Configuration")
print(output)

print("------------ Configuring loopback-----------")

cmd=["interface loopback10", "ip address 10.10.10.10 255.255.255.255", "description Management IP"]
device.send_config_set(cmd)
output = device.send_command('show ip int brief')
device.send_command('write memory')
device.disconnect()
print("------------ Output after Configuration")
print(output)
