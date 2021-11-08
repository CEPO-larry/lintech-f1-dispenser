import serial
import time
import command

'''
with serial.Serial('COM4', 9600, timeout=5, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE) as ser:
    ser.reset_input_buffer()
    ser.reset_output_buffer()

    print('enter card now')

    input('Press enter')

    # data = bytearray([0x02, 0x31, 0x35, 0x30, 0x33, 0x43, 0x50, 0x30, 0x03, 0x25]) # Collect Card
    # data = bytearray([0x02, 0x30, 0x30, 0x30, 0x33, 0x44, 0x43, 0x30, 0x03, 0x35]) # return to front port
    data = bytearray([0x02, 0x31, 0x35, 0x30, 0x33, 0x44, 0x43, 0x30, 0x03, 0x31])  # return to front port
    
    print(data.hex())
    ser.write(data)
    print('send command')

    time.sleep(0.5)
    print(ser.inWaiting())
    # x = ser.read()          # read one byte
    s = ser.read(3)        # read up to ten bytes (timeout)
    print(s.hex())

    print('sent enquiry')
    enq = bytearray([0x05, 0x31, 0x35])
    print(enq.hex())
    ser.write(enq)

    time.sleep(0.5)
    print(ser.inWaiting())
    # x = ser.read()          # read one byte
    s = ser.read(3)  # read up to ten bytes (timeout)
    print(s.hex())
    ser.close()
'''

'''
with serial.Serial('COM4', 9600, timeout=5, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE) as ser:
    ser.reset_input_buffer()
    ser.reset_output_buffer()

    data = bytearray([0x02, 0x31, 0x35, 0x46, 0x43, 0x34, 0x03, 0x34])
    ser.write(data)

    time.sleep(0.5)
    print(ser.inWaiting())
    # x = ser.read()          # read one byte
    s = ser.read(3)  # read up to ten bytes (timeout)
    print(s.hex())

    enq = bytearray([0x05, 0x31, 0x35])
    print(enq.hex())
    ser.write(enq)
    #-----------------------------------------------
    data = bytearray([0x02, 0x31, 0x35, 0x41, 0x50, 0x03, 0x14])
    ser.write(data)

    time.sleep(0.5)
    print(ser.inWaiting())
    # x = ser.read()          # read one byte
    s = ser.read(3)  # read up to ten bytes (timeout)
    print(s.hex())

    enq = bytearray([0x05, 0x31, 0x35])
    print(enq.hex())
    ser.write(enq)
    # -----------------------------------------------
    data = bytearray([0x02, 0x31, 0x35, 0x41, 0x50, 0x03, 0x14])
    ser.write(data)

    time.sleep(0.5)
    print(ser.inWaiting())
    # x = ser.read()          # read one byte
    s = ser.read(3)  # read up to ten bytes (timeout)
    print(s.hex())

    enq = bytearray([0x05, 0x31, 0x35])
    print(enq.hex())
    ser.write(enq)

    # -----------------------------------------------
    data = bytearray([0x02, 0x31, 0x35, 0x41, 0x50, 0x03, 0x14])
    ser.write(data)

    time.sleep(0.5)
    print(ser.inWaiting())
    # x = ser.read()          # read one byte
    s = ser.read(3)  # read up to ten bytes (timeout)
    print(s.hex())

    enq = bytearray([0x05, 0x31, 0x35])
    print(enq.hex())
    ser.write(enq)
'''

ackHex = bytearray([0x05, 0x31, 0x35])
with serial.Serial('COM4', 9600, timeout=5, bytesize=serial.EIGHTBITS, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE) as ser:
    ser.reset_input_buffer()
    ser.reset_output_buffer()

    commandList = command.return2Front

    for commandItem in commandList:
        data = commandItem
        ser.write(data)

        time.sleep(0.5)
        print(ser.inWaiting())
        # x = ser.read()          # read one byte
        s = ser.read(3)  # read up to ten bytes (timeout)
        print(s.hex())

        enq = ackHex
        print(enq.hex())
        ser.write(enq)





