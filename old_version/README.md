# Blynk python PMS7003예제 for 라즈베리파이  

**라즈베리파이**에서 사용되는 **Blynk python 버전**의 **PMS7003 데이터 수신**예제 코드입니다.  

https://github.com/vshymanskyy/blynk-library-python  

위 베타 버전 라이브러리를 사용한 예제 파일로 blynk.io에 업로드 된 python 라이브러리와 호환이 되지 않습니다.  
  
  
## 사용 전 필수 라이브러리  

https://github.com/vshymanskyy/blynk-library-python  
위 라이브러리를 필수로 설치해 주셔야 합니다.   

라즈베리파이에서 위 라이브러리 설치 시 아래 명령으로 실행해야 합니다.  
>(python3 사용)  
>``pip3 install blynk-library-python``  
>다운로드 실패 시 앞에 ``sudo`` 를 붙이거나, ``pip install blynk-library-python`` 등으로 시도  


blynk_python_PMS7003에 포함된 PMS7003 라이브러리 다운로드 스크립트 실행  

>``chmod +x start.sh``  
>``./start.sh``  
   
위 명령어를 입력해 라이브러리를 다운로드 해 주어야 합니다.  

## bly_PMS7003.py  
  
blynk 연결을 위한 **사용자 토큰**을 아래 *YourAuthToken*에 입력하고  
``BLYNK_AUTH =  'YourAuthToken'``  
  
 **시리얼 설정(#USE PORT)** 부분(하단 코드 참고)을 연결 방식에 맞춰 수정해준 뒤  
```
# UART / USB Serial
USB0 =  '/dev/ttyUSB0' # USB 사용시 / USB0이 아닌경우 변경 
UART =  '/dev/ttyAMA0' # UART 사용시  
  
# USE PORT  
SERIAL_PORT = UART  #연결방식에 맞춰 변경
  
#serial setting  
ser = serial.Serial(SERIAL_PORT, Speed, timeout = 1)  
```  
``sudo puthon3 bly_PMS7003.py``  
위 명령어로 실행해 주시면 됩니다.

## start.sh
PMS7003 먼지센서의 Python 용 라이브러리 다운로드 스크립트 입니다.   

아래 명령을 입력해 파일을 다운로드 해 줍니다.   
```
chmod +x start.sh  
./start.sh  
```   
PMS7003 라이브러리   
https://github.com/eleparts/PMS7003   

Blynk timer   
https://github.com/vshymanskyy/blynk-library-python   

다운로드되는 파일은 위 링크를 참고해 주시면 됩니다.   

