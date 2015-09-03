__author__ = 'empire'

import serial  # if you have not already done so
from controller.helicopter_controller import PidOutputs

class Serial(object):
    """
    Serial Class for communication with the Arduino, and hence the RC and vehicle
    """
    def __init__(self, baud=9600):
        self.serial = serial.Serial('/dev/tty.usbserial', baud)
        self.num_ppm_channels = 2;

    def output(self):
        self.serial.write('[1500, 1500]')  #May need to use numpy array here?