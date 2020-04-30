
# A crude script to log the Modbus TCP data from a single or several FLIR A310 IR cameras
	# Find or set ip address of each camera on the network
	# Adjust 'csv_header' and 'ip_list' to match the number and addresses of cameras
	# Adjust 'reg' for desired data object in the camera
		# see 'Convert EthernetIP to Modbus TCP.pdf'

	# I have used this script with four cameras at a 1 second log interval with great success

	# Many thanks to:
		# https://pymodbustcp.readthedocs.io/en/latest/

	# Casey J. Davis 2020.01.08



# python flir_a310_log_data_via_modbus.py


from pyModbusTCP.client import ModbusClient
from pyModbusTCP import utils
import datetime
import csv
import time
import os

# set working directory
os.chdir('C:\\Users\\yourusername\\Desktop\\')


# generate unique filename
csv_filename = time.strftime("%Y%m%d-%H%M%S") + ' FLIR Cams Box Average.csv'

# first row of csv file
# must have a 'timestamp X' and 'CAM X Box 1 Avg Temp [degC]' string for each camera
csv_header = ['timestamp 1','CAM 1 Box 1 Avg Temp [degC]','timestamp X','CAM X Box 1 Avg Temp [degC]',]


with open(csv_filename, 'w', newline='') as fp:

	wr = csv.writer(fp, dialect='excel')
	wr.writerow(csv_header)

	while True:
			# list of ip addresses for the cameras 
			ip_list = ['192.168.0.101', '192.168.0.X', ]

			data_temp = []

			for n in ip_list:

				c = ModbusClient(host=n, unit_id=109, auto_open=True, auto_close=True)

				if c.open():
					
				    # 4181 is the FLIR A310 register for the Box 1 Average Temperature
				    # many other options available - see 'Convert EthernetIP to Modbus TCP.pdf' 					    
				    reg = c.read_holding_registers(4181, 2)
				    ts = datetime.datetime.now().timestamp()

				    c.close()

				a= hex(reg[0])
				b= hex(reg[1])
				c = b+a[2:]
				d = int(c,16)

				T_avg_K = utils.decode_ieee(d)
				T_avg_degC = T_avg_K - 273.15

				data_temp.append(ts)
				data_temp.append(round(T_avg_degC,2))

			print(data_temp)

			wr.writerow(data_temp)
			
			# change log interval here
			# FLIR A310 registers only appear to update about three times per second
			time.sleep(1)

