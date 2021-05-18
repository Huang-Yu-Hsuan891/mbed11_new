import serial
import time

# XBee setting
serdev = '/dev/ttyUSB0'
s = serial.Serial(serdev, 9600)

s.write("+++".encode())
char = s.read(2)
print("Enter AT mode.")
print(char.decode())

s.write("ATMY 0x128\r\n".encode())
char = s.read(3)
print("Set MY 0x128.")
print(char.decode())

s.write("ATDL 0x228\r\n".encode())
char = s.read(3)
print("Set DL 0x228.")
print(char.decode())

s.write("ATID 0x1\r\n".encode())
char = s.read(3)
print("Set PAN ID 0x1.")
print(char.decode())

s.write("ATWR\r\n".encode())
char = s.read(3)
print("Write config.")
print(char.decode())

s.write("ATMY\r\n".encode())
char = s.read(4)
print("MY :")
print(char.decode())

s.write("ATDL\r\n".encode())
char = s.read(4)
print("DL : ")
print(char.decode())

s.write("ATCN\r\n".encode())
char = s.read(3)
print("Exit AT mode.")
print(char.decode())

print("start sending RPC")
while True:
    # send RPC to remote
    s.write("/getAcc/run\n\r".encode())
    char = s.read(200)
    print(char.decode())
    time.sleep(1)
    #print(line)
    #line=s.readline() # Read an echo string from mbed terminated with '\n' (RPC reply)
    #print(line)
    #time.sleep(1)

s.close()