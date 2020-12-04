#!/usr/bin/python3
import sys, getopt
import asyncore
from fakesmtpserver import FakeSMTPServer
import logging

def main(argv):
    hostname = ''
    port = ''
    outputdir = None
    try:
        opts, args = getopt.getopt(argv, "hn:p:o:", ["hostname=", "port=", "outputdirectory="])
    except getopt.GetoptError:
        print
        'main.py -n <hostname> -p <port> -o <outputdirectory>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print
            'main.py -n <hostname> -p <port> -o <outputdirectory>'
            sys.exit()
        elif opt in ("-n", "--hostname"):
            hostname = arg
        elif opt in ("-p", "--port"):
            port = arg
        elif opt in ("-o", "--outputdirectory"):
            outputdir = arg
    portnum = 2555
    if port.isnumeric():
        portnum = int(port)
    logging.info(f'FakeSMTPServer {hostname}:{port} started...')
    server = FakeSMTPServer((hostname, portnum), None)
    if outputdir:
        server.setoutputdir(outputdir)
    asyncore.loop()
    logging.info(f'FakeSMTPServer {hostname}:{port} stopped...')

if __name__ == '__main__':
    main(sys.argv[1:])


