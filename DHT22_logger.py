import Adafruit_DHT
import time
import os
import RPi.GPIO as GPIO

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED_PIN = 16
GPIO.setup(LED_PIN, GPIO.OUT)

def write_headers():
    # Open, write, and close file. 'w'=write. Previous data will be deleted
    with open('/home/pi/Documents/PythonScripts/DHT22.csv', 'w') as log:
        log.write('DateTime,Temperature,Humidity\n')

def write_temp_hum(temp,hum):
    # Open, write, and close file. 'a'=append data to end of file
    with open('/home/pi/Documents/PythonScripts/DHT22.csv', 'a') as log:
        log.write('{0},{1:0.1f},{2:0.1f}\n'.format(time.strftime('%d/%m/%y %H:%M:%S'), temp, hum))
        
def blink_led():
    GPIO.output(LED_PIN,GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(LED_PIN,GPIO.LOW)
    
write_headers()
                  
while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        blink_led()
        write_temp_hum(temperature,humidity)
        time.sleep(60)

    else:
        print('Failed to retrieve data from humidity sensor')
    