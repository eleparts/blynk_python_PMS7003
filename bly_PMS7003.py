"""
* blynk PMS7003 데이터 송신 예제
* 수정 : 2024. 02. 16
* 제작 : eleparts 부설연구소
* SW ver. 3.1.0

> 본 예제의 PMS7003 기본 연결 설정은 USB0입니다.
> Vpin
V4 - integer 0/255  : LED
V5 - string         : Value Display
V6 - string         : Value Display
V7 - string         : Value Display

기반 코드 및 필수 라이브러리 - blynk / python (Blynk Python Library V1.0.0)
https://github.com/vshymanskyy/blynk-library-python
> 공식 저장소(2.x.x 라이브러리)에서 기존 라이브러리로 변경(1.x.x 라이브러리) 
"""

import BlynkLib
import serial
import RPi.GPIO as GPIO 
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
SERIAL_PORT = USB0  #기본값 USB0, 연결방식에 맞춰 변경

#serial setting
ser = serial.Serial(SERIAL_PORT, Speed, timeout = 1)
#========================================

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Create BlynkTimer Instance
timer = BlynkTimer()

# Create Dust sensor
dust = PMS7003()



# PMS 먼지센서 정보 읽은 후 데이터 연동 함수 - 하단 타이머로 실행
def send_pms_data():
    
    ser.flushInput()
    buffer = ser.read(1024)

    if(dust.protocol_chk(buffer)):
        data = dust.unpack_data(buffer)

        print("send - PM1.0: %d | PM2.5: %d | PM10: %d" %(data[dust.DUST_PM1_0_ATM],data[dust.DUST_PM2_5_ATM],data[dust.DUST_PM10_0_ATM]) )
        # Labeled Value (Display)
        # blynk.virtual_write(5, data[dust.DUST_PM1_0_ATM])
        # blynk.virtual_write(6, data[dust.DUST_PM2_5_ATM])
        # blynk.virtual_write(7, data[dust.DUST_PM10_0_ATM])
        # Display Value
        blynk.virtual_write(5, ("PM1.0 : " + str(data[dust.DUST_PM1_0_ATM])))
        blynk.virtual_write(6, ("PM2.5 : " + str(data[dust.DUST_PM2_5_ATM])))
        blynk.virtual_write(7, ("PM10  : " + str(data[dust.DUST_PM10_0_ATM])))

        blynk.virtual_write(4,'0')


    else: 
        # protocol_chk fail
        
        print("data Err")
        blynk.virtual_write(4,'255')


# Add Timers
# timer : 설정해 둔 시간마다 실행됨
timer.set_interval(2, send_pms_data) # 2초마다 반복실행



# Start Blynk, Start timer
while True:
    blynk.run()
    timer.run()
