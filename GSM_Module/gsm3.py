
import serial
import RPi.GPIO as GPIO      
import os, time

GPIO.setmode(GPIO.BOARD)    

# Enable Serial Communication
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key

port.write('AT'+'\r\n')
rcv = port.read(10)
print rcv
time.sleep(1)

port.write('ATE0'+'\r\n')      # Disable the Echo
rcv = port.read(10)
print rcv
time.sleep(1)

port.write('AT+CMGF=1'+'\r\n')  # Select Message format as Text mode 
rcv = port.read(10)
print rcv
time.sleep(1)

port.write('AT+CNMI=2,1,0,0,0'+'\r\n')   # New SMS Message Indications
rcv = port.read(10)
print rcv
time.sleep(1)

# Sending a message to a particular Number

port.write('AT+CMGS="09974391897"'+'\r\n')
rcv = port.read(10)
print rcv
time.sleep(1)

port.write('Hello User'+'\r\n')  # Message
rcv = port.read(10)
print rcv

port.write("\x1A") # Enable to send SMS
for i in range(10):
    rcv = port.read(10)
    print rcv
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
import serial
import RPi.GPIO as GPIO      
import os, time
 
GPIO.setmode(GPIO.BOARD)    
 
# Enable Serial Communication
port = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1)
 
# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key
 
port.write('AT'+'\r\n')
rcv = port.read(10)
print rcv
time.sleep(1)
 
port.write('ATE0'+'\r\n')      # Disable the Echo
rcv = port.read(10)
print rcv
time.sleep(1)
 
port.write('AT+CMGF=1'+'\r\n')  # Select Message format as Text mode 
rcv = port.read(10)
print rcv
time.sleep(1)
 
port.write('AT+CNMI=2,1,0,0,0'+'\r\n')   # New SMS Message Indications
rcv = port.read(10)
print rcv
time.sleep
