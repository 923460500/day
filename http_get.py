# coding:utf-8

import socket
import scapy
import dpkt
import winpcapy
import pcapy
import scapy.all as scapy
from scapy.layers.http import HTTPRequest,HTTP,HTTPResponse
import json

pcap_file = r'C:\Users\cmcc\Desktop\wyf1.pcap'


def fengxi(pkt):
    flag = False
    ip_layer = pkt.getlayer('IP')
    tcp_layer = pkt.getlayer('TCP')
    if tcp_layer:
        data = {
            'time': ip_layer.time,
            "ip": {'src': ip_layer.src, 'dst': ip_layer.dst, 'version': ip_layer.version},
            "tcp": {'seq': tcp_layer.seq, 'ack': tcp_layer.ack}
        }
        if pkt.haslayer(HTTPRequest):
            data['type'] = 'request'
            http_header = pkt[HTTPRequest].fields
            http_header.pop("Headers")
            data['hearder'] = http_header
            flag = True
        elif pkt.haslayer(HTTPResponse):
            data['type'] = 'response'
            http_header = pkt[HTTPResponse].fields
            http_header.pop("Headers")
            data['hearder'] = http_header
            flag = True
        if flag:
            if 'Raw' in pkt:
                payload = pkt['Raw'].load
                if payload:
                    if isinstance(payload, str):
                        data['data'] = payload
            print
            data


scapy.sniff(offline=pcap_file, prn=fengxi)