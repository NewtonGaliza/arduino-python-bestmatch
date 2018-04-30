import serial

arduinoSerialData = serial.Serial('/dev/ttyUSB0', 9600)

while (1==1):
    if (arduinoSerialData.inWaiting() > 0):
        myData = arduinoSerialData.readline()
        print(myData)
