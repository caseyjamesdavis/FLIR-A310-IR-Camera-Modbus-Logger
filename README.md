
 A crude Python script to log Modbus TCP data from [FLIR A310](https://www.flir.com/products/a310/) IR cameras

 * Find or set ip address of each camera on the network
 * Adjust 'csv_header' and 'ip_list' to match the number and addresses of cameras
 * Adjust 'reg' for desired data object in the camera
	* see [matrix of registers](Convert_EthernetIP_to_Modbus_TCP.pdf) published by FLIR
	
I have used this script with four cameras and a one second log interval with great success.

Many thanks to **sourceperl** for the [pyModbusTCP](https://github.com/sourceperl/pyModbusTCP) Python library.
