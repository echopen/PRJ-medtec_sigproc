#!/usr/bin/env python

import socket
import struct
from array import array
import datetime
import time

UDP_IP = "192.168.1.28"
UDP_PORT = 7538

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))


def ByteToHex( byteStr ):
    """
    Convert a byte string to it's int string representation e.g. for output.
    """
    
    out = []
    for x in byteStr:
	out.append(ord( x ))

    OutList = []
    N = len(out)/4
    
    for IList in range(N):
	tmp = int(out[IList*4])+256*int(out[IList*4+1])+256*256*int(out[IList*4+2])+256*256*256*int(out[IList*4+2])
	OutList.append(tmp)

    return OutList


#-------------------------------------------------------------------------------
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d-%H%M%S')
st = "data/"+st + "_UDP-DATA.log"
print st
targetFile = open(st, 'w+')

HeaderLen = 2
FramesReceived = 0
while True:
    data, addr = sock.recvfrom((256+HeaderLen)*4) # buffer size is (256+3)*4 bytes
    #print "[", FramesReceived, "] \treceived message:\t", len(ByteToHex(data))
    DATATable = ByteToHex(data)
    print "[\t", FramesReceived,"] \treceived packet\t"
	#ByteToHex(data)
    FramesReceived = FramesReceived +1

    for x in DATATable:
	targetFile.write(str(x)+"\t")
    targetFile.write("\n")
	
