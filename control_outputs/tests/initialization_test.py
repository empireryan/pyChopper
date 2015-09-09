import struct
import time
import serial

class Serial(object):
    """
    Serial Class for communication with the Arduino, and hence the RC and vehicle
    """
    num_channels = 3
    def __init__(self, baud=115200, com_port='COM3'):
        self.serial = serial.Serial(com_port, baud)
        self.num_ppm_channels = 6
        time.sleep(2)  # wait for Arduino; yucky, but it must be done
        self.serial.flushInput()

    def output(self, val):
        self.serial.write(val)

    def send_packet(self, ppm_array):
        if len(ppm_array) is not self.num_ppm_channels:
            raise TypeError     # @todo: raise a better error
        #for elem in ppm_array:
        self.serial.write(str(ppm_array).encode('utf-8'))

ppmValues = [1500, 1500, 1500, 1500, 1500, 1500]

mySerial = Serial()
received = None
while received is None:
    received = mySerial.serial.read()

time.sleep(2)


mySerial.output(b'65535')  # indicate start of frame
mySerial.send_packet(ppmValues)  # send array
mySerial.output(struct.pack('s', '\n,'))  #indicate end of frame



