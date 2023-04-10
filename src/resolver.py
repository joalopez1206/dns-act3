import socket
import binascii
from dnslib import DNSRecord

BUFFSIZE = 10000
ADDRESS = ('localhost', 8000)
print("Initializing socket")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(ADDRESS)
while True:
    print("Waiting msg")
    msg, sender_address = sock.recvfrom(BUFFSIZE)
    print("Message received!")
    msg_hex = binascii.hexlify(msg).decode()
    print(f"{msg_hex}\n")
    #print(DNSRecord.parse(msg))
    #print()
