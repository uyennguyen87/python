# python 3
import socket

def find_service_name():
    protocol_name = 'tcp'
    for port in xrange(20,81):
        try:
            service_name = socket.getservbyport(port, protocol_name)
        except socket.error as e:
            service_name = 'n/a'

        print("Port: %s => service name %s" % (port, service_name))

if __name__ == '__main__':
    find_service_name()
