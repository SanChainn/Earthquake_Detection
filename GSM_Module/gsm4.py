import serial
import RPi.GPIO as GPIO      
import os, time
 
# Find a suitable character in a text or string and get its position
def find(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i
 
GPIO.setmode(GPIO.BOARD)    
 
# Enable Serial Communication
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)
 
# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key
 
port.write('AT'+'\r\n')
rcv = port.read(10)
print rcv
time.sleep(1)
 
#port.write('AT+CMGF=1'+'\r\n')                 # Disable the Echo
#rcv = port.read(10)
#print rcv
#time.sleep(1)
 
port.write('AT+CMGF=1'+'\r\n')            # Select Message format as Text mode 
rcv = port.read(16)
print rcv
time.sleep(1)
 
port.write('AT+CMGD=1'+'\r\n')      # New SMS Message Indications
rcv = port.read(16)
print rcv
time.sleep(1)
 
port.write('AT+CMGR=1'+'\r\n')      # Sending sms to a particular number
rcv = port.read(10)
print rcv
time.sleep(1)

port.write('ATD09974391897;'+'\r\n')      # New SMS Message Indications
rcv = port.read(16)
print rcv
time.sleep(1)
while True:
	rcv = port.read(16)
	print rcv

