# python 3
import socket
import threading
import socketserver
SERVER_HOST = 'localhost'
SERVER_PORT = 0  # tells the kernel to pick up a port dynamically
BUF_SIZE = 1024


def client(ip, port, message):
    """ A client to test threading mixin server """

    # Connect to the server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(BUF_SIZE), 'ascii')
        print("Client received: {}".format(response))
    finally:
        sock.close()


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    """ An example of threaded TCP request handler """

    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
        current_thread = threading.current_thread()
        response = "{}: {}".format(current_thread.name, data)
        self.request.sendall(bytes(response, 'ascii'))


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """ Nothing to add here, inherited everything necessary from parents """
    pass

if __name__ == '__main__':
    # Run server
    server = ThreadedTCPServer((SERVER_HOST, SERVER_PORT),
                               ThreadedTCPRequestHandler)
    ip, port = server.server_address  # retrive ip server_address
    # Start a thread with the server -- one thread per request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread exits
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running on thread: {}".format(server_thread.name))
    # Run client
    client(ip, port, "Hello from client 1")
    client(ip, port, "Hello from client 2")
    client(ip, port, "Hello from client 3")
    # Server clean up
