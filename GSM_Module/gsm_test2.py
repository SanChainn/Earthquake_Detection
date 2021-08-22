import serial
import time

print "Start TTYS0 9600"
print "--------------------------"
port = serial.Serial("/dev/ttyS0",baudrate=9600, timeout=1)
time.sleep(1)

port.write('AT'+'\r\n')
rcv  = port.read(10)
print rcv
print "AT Command ttyS0 9600 "
time.sleep(1)



port = serial.Serial("/dev/ttyS0",baudrate=115200, timeout=1)
time.sleep(1)
port.write('AT'+'\r\n')
rcv  = port.read(10)
print rcv
print "AT Command ttyS0 115200"
time.sleep(1)





