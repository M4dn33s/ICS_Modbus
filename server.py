#!/usr/bin/env python

# --------------------------------------------------------------------------- # 
# import the various server implementations
# --------------------------------------------------------------------------- #
from pymodbus.version import version
from pymodbus.server.asynchronous import StartTcpServer
from pymodbus.server.asynchronous import StartUdpServer
from pymodbus.server.asynchronous import StartSerialServer

from pymodbus.device import ModbusDeviceIdentification # for challenge critical.
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import (ModbusRtuFramer,
                                  ModbusAsciiFramer,
                                  ModbusBinaryFramer)
#from custom_message import CustomModbusRequest # not require

# --------------------------------------------------------------------------- # 
# configure the service logging  - good for monitoring
# --------------------------------------------------------------------------- # 
import logging
FORMAT = ('%(asctime)-15s %(threadName)-15s'
          ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger()
log.setLevel(logging.DEBUG)


def run_async_server():
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [17]*100),
        co=ModbusSequentialDataBlock(0, [17]*100),
        hr=ModbusSequentialDataBlock(0, [17]*100),
        ir=ModbusSequentialDataBlock(0, [17]*100))
    context = ModbusServerContext(slaves=store, single=True)
    
    # ----------------------------------------------------------------------- # 
    # initialize the server information
    # ----------------------------------------------------------------------- # 
    # If you don't set this or any fields, they are defaulted to empty strings.
    # ----------------------------------------------------------------------- # 
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'ICS_KSA'
    identity.ProductCode = 'LT'
    identity.VendorUrl = 'Twitter:@Fahadx1337'
    identity.ProductName = 'Level Transmitter'
    identity.ModelName = 'Beta version'
    identity.__setitem__(0x82, "CTF{Modbus_!s_s0_s3cur3}"); # adding more info through memory address
    identity.MajorMinorRevision = "1.0.1b"
    
    # ----------------------------------------------------------------------- # 
    # run the server you want
    # ----------------------------------------------------------------------- # 

    # TCP Server
    # Adjust address unless you want on all interfaces
    StartTcpServer(context, identity=identity, address=("0.0.0.0", 502),
                   )


if __name__ == "__main__":
    run_async_server()
