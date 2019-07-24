"""
* blynk로 PMS7003 데이터 송신 예제
* 수정 : 2019. 07. 24
* 제작 : eleparts 부설연구소
* SW ver. 2.0.0

2.0.0 변경사항
> blynk.io 홈페이지에 업로드된 라이브러리로 대체되었습니다. 
>기존 버전은 old_version 디렉터리로 이동됨

>본 예제의 PMS7003 기본 연결 설정이 USB0로 변경되었습니다.
> Vpin 7,8,9 = LCD 
> Vpin 6 = LED

기반 코드 및 필수 라이브러리 - blynk / python (Blynk Python Library V0.2.4)
https://github.com/blynkkk/lib-python
"""

import blynklib
import blynktimer
import time
import serial
import RPi.GPIO as GPIO 
from PMS7003 import PMS7003


BLYNK_AUTH = 'YourAuthToken'

#========================================
# Baud Rate
Speed = 9600

# UART / USB Serial
USB0 = '/dev/ttyUSB0'
UART = '/dev/ttyAMA0'

# USE PORT  
SERIAL_PORT = USB0  #기본값 USB0, 연결방식에 맞춰 변경

#serial setting 
ser = serial.Serial(SERIAL_PORT, Speed, timeout = 1)
#========================================

# Initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

# Create BlynkTimer Instance
timer = blynktimer.Timer()

# Create Dust sensor
dust = PMS7003()


# Add Timers
# timer : 설정해 둔 시간마다 실행됨
@timer.register(interval=2, run_once=False) # 2초마다 반복실행
def my_user_task():
  # do any non-blocking operations
  
  ser.flushInput()
  buffer = ser.read(1024)

  if(dust.protocol_chk(buffer)):
    data = dust.unpack_data(buffer)

    print("send - PM1.0: %d | PM2.5: %d | PM10: %d" %(data[dust.DUST_PM1_0_ATM],data[dust.DUST_PM2_5_ATM],data[dust.DUST_PM10_0_ATM]) )
    # Labeled Value (Display)
    blynk.virtual_write(7, data[dust.DUST_PM1_0_ATM])
    blynk.virtual_write(8, data[dust.DUST_PM2_5_ATM])
    blynk.virtual_write(9, data[dust.DUST_PM10_0_ATM])
    # Value Display
    #blynk.virtual_write(7, ("PM1.0 : " + str(data[dust.DUST_PM1_0_ATM])))
    #blynk.virtual_write(8, ("PM2.5 : " + str(data[dust.DUST_PM2_5_ATM])))
    #blynk.virtual_write(9, ("PM10  : " + str(data[dust.DUST_PM10_0_ATM])))

    blynk.virtual_write(6,'0')
  
  
  else: 
    # protocol_chk fail
    
    print("data Err")
    blynk.virtual_write(6,'255')



# Start Blynk, Start timer
while True:
  blynk.run()
  timer.run()
