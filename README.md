# Blynk python PMS7003예제 for 라즈베리파이  

**라즈베리파이**에서 사용되는 **Blynk python 버전**의 **PMS7003 데이터 수신**예제 코드입니다.  
Blynk python 구성품 키트 정보는 아래 페이지를 참고 해 주세요  

라즈베리파이 IOT 키트 V2.0  
https://www.eleparts.co.kr/EPXMVGDB  

**위 IOT 키트와 관련된 전체 예제는 아래 페이지에서 확인 가능합니다.**  
https://github.com/eleparts/iotkit  
  
  
## 사용 전 필수 라이브러리  

https://github.com/vshymanskyy/blynk-library-python  
위 라이브러리를 필수로 설치해 주셔야 합니다.  
   
라즈베리파이에서 라이브러리 설치 시 아래 명령으로 실행해야 합니다.  

```bash
# 복제된 lynk-library-python 라이브러리
git clone https://github.com/eleparts/blynk-library-python
cd blynk-library-python
sudo python setup.py install
```

만약 라즈베리파이5를 사용한다면 아래 명령어로 pi5 GPIO 라이브러리를 설치해 주어야 합니다.

```bash
# 반드시 라즈베리파이 5 사용시에만 설치
pip install --break-system-packages rpi-lgpio
```
  
blynk_python_PMS7003 다운로드 및 포함된 PMS7003 라이브러리 다운로드 스크립트 실행  
  
>``git clone https://github.com/eleparts/blynk_python_PMS7003``  
>``chmod +x start.sh``  
>``./start.sh``  
  
위 명령어를 입력해 라이브러리를 다운로드 해 주어야 합니다.  
(다운로드 되는 라이브러리는 하단 start.sh 참고)  
  
  
## bly_PMS7003.py  
  
blynk 연결을 위한 **사용자 토큰**을 아래 *YourAuthToken*에 입력하고  
``BLYNK_AUTH =  'YourAuthToken'``  
  
 **시리얼 설정(#USE PORT)** 부분(하단 코드 참고)을 연결 방식에 맞춰 수정해준 뒤  
```
# UART / USB Serial
USB0 =  '/dev/ttyUSB0' # USB 사용시 / USB0이 아닌경우 변경 
UART =  '/dev/ttyAMA0' # UART 사용시  
  
# USE PORT  
SERIAL_PORT = USB0  #연결방식에 맞춰 변경, 기본값 USB0 로 변경됨
  
#serial setting  
ser = serial.Serial(SERIAL_PORT, Speed, timeout = 1)  
```  
``sudo python3 bly_PMS7003.py``  
위 명령어로 실행해 주시면 됩니다.
  
※ blynk 위젯 배치  
> Vpin 7,8,9 = LCD   
> Vpin 6 = LED  
  
## start.sh  
PMS7003 먼지센서의 Python 용 라이브러리 다운로드 스크립트 입니다.   

아래 명령을 입력해 파일을 다운로드 해 줍니다.   
```
chmod +x start.sh  
./start.sh  
```   
PMS7003 라이브러리   
https://github.com/eleparts/PMS7003   
  
다운로드되는 파일은 위 링크를 참고해 주시면 됩니다.  
  
  
## old_version  

구버전(1.x.x / 2.x.x) 파일이 정리되어 있습니다.  
  