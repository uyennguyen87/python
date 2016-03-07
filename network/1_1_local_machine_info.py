# python3
import socket

def get_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    return {
        'host_name': host_name,
        'ip_address': ip_address
    }


def print_machine_info():
    info = get_machine_info()
    print("Host name: %s" % info['host_name'])
    print("IP address: %s" % info['ip_address'])

if __name__ == '__main__':
    print_machine_info()