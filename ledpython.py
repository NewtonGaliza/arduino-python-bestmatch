from pyfirmata import Arduino, util
import time

board=Arduino('/dev/ttyUSB0')
for i in range(10):
    print('Piscando ',i)
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)
