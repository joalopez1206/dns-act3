from __future__ import annotations
import logging
import socket
from dnslib import DNSRecord, DNSHeader, DNSQuestion, RR
from dnslib.dns import CLASS, QTYPE
# Seteando el logger para la parte 4
logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] --> %(message)s')
ADDR = ("192.33.4.12", 53)
BUFFSIZE = 10000
ADDRESS = ('localhost', 8000)


def has_type_a_answer(lista: list[RR]) -> bool:
    return any(map(lambda x: QTYPE.get(x.rtype) == 'A', lista))


def answer_delegates_to_ns(parsed_dns_msg: DNSRecord) -> bool:
    return True


def get_type_a_answer(lista: list[RR]) -> tuple[str, str]:
    for x in lista:
        if QTYPE.get(x.rtype) == 'A':
            #logging.debug(x)
            return x.get_rname(), x.rdata


def resolver(mensaje_consulta: bytes, ip: str = ADDR[0], port: int = ADDR[1], buffsize: int = BUFFSIZE) -> bytes | None:
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    logging.debug(f'Sending message {mensaje_consulta}')
    sender_socket.sendto(mensaje_consulta, (ip, port))
    received_msg, receiver_addrs = sender_socket.recvfrom(buffsize)
    logging.debug(f'Received message {received_msg}')
    parsed_dns_msg = DNSRecord.parse(received_msg)
    logging.debug(f'Parsed message\n{parsed_dns_msg}')
    # Primer caso(si ocurre que no hay elementos de respuesta)
    list_of_records = parsed_dns_msg.rr
    logging.debug(f'List of records {list_of_records}')
    logging.debug(has_type_a_answer(list_of_records))
    if has_type_a_answer(list_of_records):
        logging.debug('Message has type A answer in records! returning message')
        return mensaje_consulta
    elif answer_delegates_to_ns(parsed_dns_msg):
        logging.debug('Message does not have type A answer, searching...')
        list_additional_records = parsed_dns_msg.ar
        logging.debug(f'list of additional records:\n\t{list_additional_records}\n\thas type answer:{has_type_a_answer(list_additional_records)}')
        if has_type_a_answer(list_additional_records):
            qname, ip_answer = get_type_a_answer(list_additional_records)
            parsed_dns_msg.add_answer(*RR.fromZone(f"{qname} A {ip_answer}"))
            #logging.debug(parsed_dns_msg)
            return resolver(parsed_dns_msg.pack(), ip=ip_answer)
        else:
            ...
    else:
        print("Not specified!")
        return None


print("Initializing socket")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(ADDRESS)
while True:
    print("Waiting msg")
    msg, sender_address = sock.recvfrom(BUFFSIZE)
    logging.debug("Message received!")
    resolver(msg)
    # dns_message_parsed = DNSRecord.parse(msg)
    # print("=" * 20)
    # print(dns_message_parsed.rr)
    # print("=" * 20)
