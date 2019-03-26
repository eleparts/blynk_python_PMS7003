"""
* blynk로 PMS7003 데이터 송신 예제
* 수정 : 2019. 03. 26
* 제작 : eleparts 부설연구소
* SW ver. 1.1.0
"""

import BlynkLib
import time
import serial
from PMS7003 import PMS7003
from BlynkTimer import BlynkTimer

BLYNK_AUTH = 'YourAuthToken'

#========================================
# Baud Rate
Speed = 9600

# UART / USB Serial
USB0 = '/dev/ttyUSB0'
UART = '/dev/ttyAMA0'

# USE PORT  
SERIAL_PORT = UART  #연결방식에 맞춰 변경

#serial setting 
ser = serial.Serial(SERIAL_PORT, Speed, timeout = 1)
#========================================

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Create BlynkTimer Instance
timer = BlynkTimer()

dust = PMS7003()


# (period must be a multiple of 50 ms)
def my_user_task():
  # do any non-blocking operations
  
  ser.flushInput()
  buffer = ser.read(1024)

  if(dust.protocol_chk(buffer)):
    data = dust.unpack_data(buffer)

    print("send - PM1.0: %d | PM2.5: %d | PM10: %d" %(data[dust.DUST_PM1_0_ATM],data[dust.DUST_PM2_5_ATM],data[dust.DUST_PM10_0_ATM]) )
    blynk.virtual_write(4, data[dust.DUST_PM1_0_ATM])
    blynk.virtual_write(5, data[dust.DUST_PM2_5_ATM])
    blynk.virtual_write(6, data[dust.DUST_PM10_0_ATM])
    # blynk.virtual_write(6, ('PM10  : ' + str(data[dust.DUST_PM10P0_ATM])))

    blynk.virtual_write(1,'0')
  
  
  else: 
    # protocol_chk fail
    
    print("data Err")
    blynk.virtual_write(1,'255')



# Add Timers
# Will Print Every 2 Seconds
timer.set_interval(2, my_user_task)

# Start Blynk, Start timer
while True:
  blynk.run()
  timer.run()