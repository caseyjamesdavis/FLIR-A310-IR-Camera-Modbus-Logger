
 Log Temperature Data from [FLIR A310](https://www.flir.com/products/a310/) IR cameras to a CSV file using MODBUS TCP and Python.
 
 * Get the ip address of each camera on the network
 * In flir_a310_log_data_via_modbus.py Adjust the lists 'csv_header' and 'ip_list' to match the number and addresses of cameras
 * Adjust 'reg' variable for desired data object in the camera
	* see [matrix of registers](Convert_EthernetIP_to_Modbus_TCP.pdf) published by FLIR
* Run flir_a310_log_data_via_modbus.py
	
I have tested this with four cameras and a one second log interval.

Many thanks to **sourceperl** for the [pyModbusTCP](https://github.com/sourceperl/pyModbusTCP) Python library.
