#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 Prashant Anantharaman <prashant.anantharaman@sri.com> %>
#
"""

"""
import pdb
import sys
import pyshark
import numpy as np
import os
import pcap
import dpkt
from dpkt.ip import IP
from dpkt.tcp import TCP
from dpkt.http import Request
from dpkt.http import Response

# pcap = pcap.pcap('/home/prashant/Downloads/setpoint.pcap')
def get_array(pkt):
    pdb.set_trace()
    if pkt.highest_layer == 'MQTT':
        print(pkt.tcp._all_fields['tcp.pdu.size'].all_fields[0].raw_value)
        
pcap_file = sys.argv[1]
cap = pyshark.FileCapture(pcap_file)
#get_array(pcap_file)
cap.apply_on_packets(get_array)
