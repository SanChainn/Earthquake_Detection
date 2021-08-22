
import smbus			#import SMBus module of I2C
from time import sleep          #import
import time

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47

count = 0

def MPU_Init():
	#write to sample rate register
	bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)
	
	#Write to power management register
	bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
	
	#Write to Configuration register
	bus.write_byte_data(Device_Address, CONFIG, 0)
	
	#Write to Gyro configuration register
	bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
	
	#Write to interrupt enable register
	bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
	#Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)
    
        #concatenate higher and lower value
        value = ((high << 8) | low)
        
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value


bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address

MPU_Init()

print (" Reading Data of Gyroscope and Accelerometer")

while True:

	#Read Accelerometer raw value
	acc_x = read_raw_data(ACCEL_XOUT_H)
	acc_y = read_raw_data(ACCEL_YOUT_H)
	acc_z = read_raw_data(ACCEL_ZOUT_H)


	#Full scale range +/- 250 degree/C as per sensitivity scale factor
	Ax = acc_x/16384.0
	Ay = acc_y/16384.0
	Az = acc_z/16384.0

	local = time.asctime(time.localtime(time.time()))
		
	Ax ="{:.2f}".format(Ax)
	Ax = float(Ax)

	Ay ="{:.2f}".format(Ay)
	Ay = float(Ay)

	Az ="{:.2f}".format(Az)
	Az = float(Az)	
	
	print(" ")
	print("----------------------------------------")
	print(f"Ax = {Ax}  , AY =  {Ay}  , AZ = {Az} ")
	
	
	#testing for level 1 earthquake	
	if -0.07 <= Ax <= -0.01 and -0.06 <= Ay <= 0.00 :
		print(" ")
		print(f"Earthquake is :: LEVEL 1 \nTime :{local}")
		print(" ")
		print("----------------------------------------")
		count+=1

	elif (-0.20 <= Ax <= 0.20 and -0.11 <= Ay <= 0.01) or (-0.08 <= Ax <= -0.01 and -0.20 <= Ay <= 0.20) :
		print(" ")
		#green color 
		print(f"\033[1;32;40m Earthquake is :: LEVEL 2 \nTime :{local}")
		print(" ")
		print("---------------------------------------- \033[0m ")
		count+=1	

	elif (-0.50 <= Ax <= 0.50 and -0.25 <= Ay <= 0.25) or (-0.25 <= Ax <= 0.25 and -0.50 <= Ay <= 0.50) :
		print(" ")
		#Cyan
		print(f"\033[1;36;40m Earthquake is :: LEVEL 3 \nTime :{local}")
		print(" ")
		print("---------------------------------------- \033[0m")
		count+=1	
	
	elif (-0.80 <= Ax <= 0.80 and -0.45 <= Ay <= 0.45) or (-0.45 <= Ax <= 0.45 and -0.80 <= Ay <= 0.80) :
		print(" ")
		#Purple
		print(f"\033[1;35;40m Earthquake is :: LEVEL 4 \nTime :{local}")
		print(" ")
		print("---------------------------------------- \033[0m")
		count+=1

	elif (-1.4 <= Ax <= 1.4 and -0.70 <= Ay <= 0.70) or (-0.70 <= Ax <= 0.70 and -1.4 <= Ay <= 1.4) :
		print(" ")
		#Yello 
		print(f"\033[1;33;40m Earthquake is :: LEVEL 5 \nTime :{local}")
		print(" ")
		print("---------------------------------------- \033[0m ")
		count+=1

	elif (-2.0 <= Ax <= 2.0 and -1.10 <= Ay <= 1.10) or (-1.10 <= Ax <= 1.10 and -2.0 <= Ay <= 2.0) :
		print(" ")
		#RED
		print(f"\033[1;31;40m Earthquake is :: LEVEL 6 \nTime :{local} \033[0m")
		print("---------------------------------------- \033[0m")
		count+=1	

	else:
		print(f"Other :{count}")	
		print("-----------------------------------------------------------------------------")
		print("-----------------------------------------------------------------------------")		
		count=0
	sleep(0.3)
	
