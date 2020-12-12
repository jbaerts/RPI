import Adafruit_DHT
import time
import os

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

running = True

try:
    file = open('/home/pi/Documents/PythonScripts/DHT22.csv', 'w')
    file.write('DateTime,Temperature,Humidity\n')

except:
    pass

while running:
    try:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        if humidity is not None and temperature is not None:
            file.write('{0},{1:0.1f},{2:0.1f}\n'.format(time.strftime('%d/%m/%y %H:%M:%S'), temperature, humidity))
            time.sleep(60)

        else:
            print('Failed to retrieve data from humidity sensor')
    
    except KeyboardInterrupt:
        print ('Program stopped')
        running = False
        file.close()