'''
Created on 03.02.2020

@author: Jan-Erik Matthies
'''
from Tca9548A import Tca9548A
from smbus2 import SMBus

#default address of the Tca9548A
tcaAddress = 0x70
#your I2C bus
i2cBus = SMBus(1)
#the multiplexer channel (0 to 7) your i2c device(s) is connected to
multiplexerChannelNr0 = 0 
multiplexerChannelNr7 = 7
#create yout 
tca = Tca9548A(i2cBus = i2cBus, address = tcaAddress)
#get the channel your i2c device is connected to 
bus0 = tca.getChannel(multiplexerChannelNr0)
bus7 = tca.getChannel(multiplexerChannelNr7)
#your bus0 to bus7 behave exactly the same way your smbus2.SMBus(1) would do.
b = bus0.read_byte_data(80, 0)
print(b)
b = bus7.read_byte_data(80, 0)
print(b)