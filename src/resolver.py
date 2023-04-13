import socket
import binascii
from dnslib import DNSRecord

def resolver(mensaje_consulta):
    ...
PATH = 'input.txt'
BUFFSIZE = 10000
ADDRESS = ('localhost', 8000)
print("Initializing socket")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(ADDRESS)
while True:
    print("Waiting msg")
    msg, sender_address = sock.recvfrom(BUFFSIZE)
    print("Message received!")
    with open(PATH, 'w+b') as file:
        file.write(msg)
    #print(msg)
    ## Forma facil de hacer un parser
    dns_message_parsed = DNSRecord.parse(msg)
    #TODO
    # La forma mas dificil seria leer de un archivo cada byte e usar la especificacion
    # para ver que es cada dato que encontramos.
