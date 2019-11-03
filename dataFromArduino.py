import serial
import re
import bluetooth

ser = serial.Serial('/dev/ttyUSB0', 115200)
while 1:
    if(ser.in_waiting >0):
        line = ser.readline()
        #"roll:angle1;pitch:angle2"
        data = re.split(': |; ', line)
        roll = int(data[1])
        pitch = int(data[3])

host = ""
port = 1	# Raspberry Pi uses port 1 for Bluetooth Communication
# Creaitng Socket Bluetooth RFCOMM communication
server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print('Bluetooth Socket Created')
try:
	server.bind((host, port))
	print("Bluetooth Binding Completed")
except:
	print("Bluetooth Binding Failed")
server.listen(1) # One connection at a time
# Server accepts the clients request and assigns a mac address. 
client, address = server.accept()
print("Connected To", address)
print("Client:", client)
try:
	while True:
		# Receivng the data. 
		data = client.recv(1024) # 1024 is the buffer size.
		print(data)
		
		if data == "1":
			GPIO.output(led_pin, True)
			send_data = "Light On "
		elif data == "0":
			GPIO.output(led_pin, False)
			send_data = "Light Off "
		else:
			send_data = "Type 1 or 0 "
		# Sending the data.
		client.send(send_data) 
except:
	# Making all the output pins LOW
	GPIO.cleanup()
	# Closing the client and server connection
	client.close()
	server.close()