#-----------------------------------------------------------------------------
#Copyright (c) Peter Bingham  (petersbingham@hotmail.co.uk)
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
#-----------------------------------------------------------------------------

import re
from . import dae_RelayBoard_Common
from pylibftdi import BitBangDevice, Driver
            
class FTD2XXLinux(object):
    def __init__(self):
        self.driver = Driver()
        self.bb = None
        self.comport = None
 
    def initialise(self, deviceID, baudRate, mask, bitMode):
        try:
            for dev in self.driver.list_devices():
                if re.search(deviceID + '.+', dev[2].decode()):
                    deviceID = dev[2]
                    print('Found device ' + deviceID.decode())
                    break
            if deviceID is None:
                raise dae_RelayBoard_Common.Denkovi_Exception('No board connected')

            self.bb = BitBangDevice(deviceID.decode())
            self.bb.direction = mask
            self.bb.open()
        except Exception as e:
            raise dae_RelayBoard_Common.Denkovi_Exception('Could not connect to relay board: %s: %s' % (e.__class__, e))
 
    def close(self):
        pass
        
    def writeByte(self, byte):
        if self.bb is None:
            raise dae_RelayBoard_Common.Denkovi_Exception('Board non initialized')
        self.bb.port = byte
 
    def readByte(self):
        if self.bb is None:
            raise dae_RelayBoard_Common.Denkovi_Exception('Board non initialized')
        return self.bb.port
        
