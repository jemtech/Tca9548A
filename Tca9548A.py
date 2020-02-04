'''
Created on 23.01.2020

@author: Jan-Erik Matthies
'''
import smbus2
from threading import Lock

class Tca9548A(object):
    '''
    handles communication and setup of a TCA9548A
    '''

    def __init__(self, i2cBus = None, address = 0x70):
        '''
        Constructor
        '''
        self.address = address
        if i2cBus is None:
            self.bus = smbus2.SMBus(1)
        else:
            self.bus = i2cBus
            
    def getChannel(self, channel):
        '''
        returns the Tca9548AChannel for communication
        '''
        return Tca9548AChannel(self,channel)
    
    def disable(self):
        '''
        disables the chip output to prevent collisions with other bus clients 
        '''
        self.bus.write_byte(self.address, 0)
    
    def openChannel(self, channel):
        '''
        activates the selected output 0 to 8 is possible
        '''
        self.bus.write_byte(self.address, channel)

class Tca9548AChannel(object):
    '''
    use like smbus2
    thread safe i2c bus wrapper
    caring about opening and closing the channels of the TCA9548A
    preventing collisions
    '''
    def __init__(self, tca9548A, channel):
        '''
        Constructor
        '''
        #2 power channel number because it is the register bit
        self.channel = 2**channel
        self.tca9548A = tca9548A
        
    def __transaction(self, method, *args, **kwargs):
        lock.acquire()
        try:
            self.tca9548A.openChannel(self.channel)
            result = method(*args, **kwargs)
            self.tca9548A.disable()
        finally:
            lock.release()
        return result
            
    def read_word_data(self, *args, **kwargs):
        return self.__transaction(self.tca9548A.bus.read_word_data, *args, **kwargs)
    
    def read_byte_data(self, *args, **kwargs):
        return self.__transaction(self.tca9548A.bus.read_byte_data, *args, **kwargs)
    
    def process_call(self, *args, **kwargs):
        return self.__transaction(self.tca9548A.bus.process_call, *args, **kwargs)
        
    def block_process_call(self, *args, **kwargs):
        return self.__transaction(self.tca9548A.bus.block_process_call, *args, **kwargs)
        
    def read_block_data(self, *args, **kwargs):
        return self.__transaction(self.tca9548A.bus.read_block_data, *args, **kwargs)
        
    def read_byte(self, *args, **kwargs):
        return self.__transaction(self.tca9548A.bus.read_byte, *args, **kwargs)
        
    def read_i2c_block_data(self, *args, **kwargs):
        return self.__transaction(self.tca9548A.bus.read_i2c_block_data, *args, **kwargs)
        
    def write_block_data(self, *args, **kwargs):
        return self.__transaction(self.tca9548A.bus.write_block_data, *args, **kwargs)
        
    def write_byte(self, *args, **kwargs):
        return self.__transaction(self.tca9548A.bus.write_byte, *args, **kwargs)
        
    def write_byte_data(self, *args, **kwargs):
        return self.__transaction(self.tca9548A.bus.write_byte_data, *args, **kwargs)
        
    def write_i2c_block_data(self, *args, **kwargs):
        return self.__transaction(self.tca9548A.bus.write_i2c_block_data, *args, **kwargs)
        
    def write_quick(self, *args, **kwargs):
        return self.__transaction(self.tca9548A.bus.write_quick, *args, **kwargs)
        
    def write_word_data(self, *args, **kwargs):
        return self.__transaction(self.tca9548A.bus.write_word_data, *args, **kwargs)
        
class Pipe(object):
    
    def __init__(self, bus, address, force = None):
        self.bus = bus
        self.address = address
        self.force = force
            
    def read_word_data(self, register):
        return self.bus.read_word_data(i2c_addr = self.address, register = register, force = self.force)
    
    def read_byte_data(self, register):
        return self.bus.read_byte_data(i2c_addr = self.address, register = register, force = self.force)    
    
    def process_call(self, register, value):
        return self.bus.process_call(i2c_addr = self.address, register = register, value = value, force = self.force)
        
    def block_process_call(self, register, data):
        return self.bus.block_process_call(i2c_addr = self.address, register = register, data = data, force = self.force)
        
    def read_block_data(self, register):
        return self.tca9548A.bus.read_block_data(i2c_addr = self.address, register = register, force = self.force)
        
    def read_byte(self):
        return self.tca9548A.bus.read_byte(i2c_addr = self.address, force = self.force)
        
    def read_i2c_block_data(self, register, length):
        return self.bus.read_i2c_block_data(i2c_addr = self.address, register = register, length = length, force = self.force)
        
    def write_block_data(self, register, data):
        return self.bus.write_block_data(i2c_addr = self.address, register = register, data = data, force = self.force)
        
    def write_byte(self, value):
        return self.bus.write_byte(i2c_addr = self.address, value = value, force = self.force)
        
    def write_byte_data(self, register, value):
        return self.tca9548A.bus.write_byte_data(i2c_addr = self.address, register = register, value = value, force = self.force)
        
    def write_i2c_block_data(self, register, data):
        return self.bus.write_i2c_block_data(i2c_addr = self.address, register = register, data = data, force = self.force)
        
    def write_quick(self):
        return self.bus.write_quick(i2c_addr = self.address, force = self.force)
        
    def write_word_data(self, register, value):
        return self.bus.write_word_data(i2c_addr = self.address, register = register, value = value, force = self.force)
    
lock = Lock()
        