
import smbus            #import SMBus module of I2C
from time import sleep          #import
import time
from datetime import datetime

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


bus = smbus.SMBus(1)    # or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address

MPU_Init()

print (" Reading Data of Gyroscope and Accelerometer")
f = open('example.txt','w')
f.write("")
f.close()

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
    i = int((Ax*3 + Ay*4 + Az*5 ) *2)
    
    #testing for level 1 earthquake 
    
    f = open('example.txt','a')
    timeC = time.strftime("%I")+" : "+time.strftime("%M")+" : "+time.strftime("%S")
    aa = timeC+","+str(i)
    sleep(1)
    f.write(aa)
    print(aa)
    f.write("\n")
    f.close()
    
    #sleep(0.3)
    
