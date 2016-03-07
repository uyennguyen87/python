# python 3
import socket

def get_remote_machine_info(remote_host):
    try:
        print("IP address: %s" % socket.gethostbyname(remote_host))
    except socket.error as e:
        print("%s: %s" % (remote_host, e))

if __name__ == "__main__":
    get_remote_machine_info('www.python.org')
