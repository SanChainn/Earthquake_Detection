from gpiozero import LED
import smbus            #import SMBus module of I2C
from time import sleep          #import
import time
from datetime import datetime
import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
from time import sleep
from datetime import datetime

import serial

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

plt.style.use('fivethirtyeight')

x_values = []
y_values = []
level = ""

buzzer = LED(14)
led_red = LED(16)
led_yellow = LED(20)
led_green = LED(21)

f = open('example.txt','w')
f.write("")
f.write("From Raspberry pi")
f.write("\n")
f.write("  TIME         :: Data  \t   :: LEVEL ")
f.write("\n")
f.write("------------------------------------")
f.write("\n")
f.close()


ser = serial.Serial("/dev/ttyACM0",9600,timeout=1)
ser.flush()

def led_off():
    led_red.off()
    led_yellow.off()
    led_green.off()


def animate(i):
    
    #Read Accelerometer raw value
    acc_x = read_raw_data(ACCEL_XOUT_H)
    #acc_y = read_raw_data(ACCEL_YOUT_H)
    #acc_z = read_raw_data(ACCEL_ZOUT_H)


    #Full scale range +/- 250 degree/C as per sensitivity scale factor
    Ax = acc_x/16384.0
    #Ay = acc_y/16384.0
    #Az = acc_z/16384.0

    local = time.asctime(time.localtime(time.time()))
        
    Ax ="{:.2f}".format(Ax)
    Ax = float(Ax)

    #Ay ="{:.2f}".format(Ay)
    #Ay = float(Ay)

    #Az ="{:.2f}".format(Az)
    #Az = float(Az)  
    
    print(" ")
    print("----------------------------------------")
    #print(f"Ax = {Ax}  , AY =  {Ay}  , AZ = {Az} ")
    print(f"Ax = {Ax}  ")
    i = int(Ax*100)
    if (120 >= i >= -120):
    
        timeC = time.strftime("%I")+" : "+time.strftime("%M")+" : "+time.strftime("%S")
        x_values.append(timeC)
        y_values.append(i)

        if ( 20 >= i >= -20):
            level = "LEVEL 1"
            buzzer.on()
            sleep(1)
            buzzer.off()
            sleep(1)
            print(level)
        elif ( 40 >= i >= -40):
            level = "LEVEL 2"
            
            total = " Earthquake Data From Raspberry Pi \n TIME       :: Data  \t   :: LEVEL \n"+timeC+" :: "+str(i)+"\t   :: "+level
            total = total.encode()
            ser.write(total)
            led_off()
            led_green.on()
            print(level)
        elif ( 60 >= i >= -60):
            level = "LEVEL 3"
            buzzer.on()
            sleep(1)
            buzzer.off()
            sleep(1)
            print(level)
        elif ( 80 >= i >= -80):
            level = "LEVEL 4"
            total = " Earthquake Data From Raspberry Pi \n TIME       :: Data  \t   :: LEVEL \n"+timeC+" :: "+str(i)+"\t   :: "+level
            total = total.encode()
            ser.write(total)
            led_off()
            led_yellow.on()
            
            print(level)
        elif ( 100 >= i >= -100):
            level = "LEVEL 5"
            print(level)
        elif ( 120 >= i >= -120):
            level = "LEVEL 6"
            led_off()
            led_red.on()
            print(level)
       
    
        f=open('example.txt','a')
        total = timeC+" :: "+str(i)+"\t   :: "+level
        f.write(total)
        f.write('\n')
        f.close()
        print(total)

    plt.cla()
    plt.plot(x_values, y_values,'ro-',linewidth=1)

    plt.ylabel('LEVEL')
    plt.xlabel('TIME')
    plt.xticks(rotation=45)
    plt.xticks(fontsize=10)
    plt.title('Earthquake LEVEL ')
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    
    sleep(0.6)

ani = FuncAnimation(plt.gcf(), animate, 1000)

plt.tight_layout()
plt.show()



    
