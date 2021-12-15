import socket
import struct

HOST = socket.gethostbyname("")
# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

s.bind((HOST, 0))

s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

n = 1
while (n <= 400):
    print('Number ', n)
    data = s.recvfrom(3000)
    packet = data[0]
    address = data[1]
    header = struct.unpack('!BBHHHBBHBBBBBBBB', packet[:20])
    print(address, packet, header)
