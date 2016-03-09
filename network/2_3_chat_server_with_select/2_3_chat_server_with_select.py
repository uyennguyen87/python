import select
import socket
import sys
import signal
import pickle
import struct
import argparse

SERVER_HOST = 'localhost'
CHAT_SERVER_NAME = 'server'


# Some utilities
def send(channel, *args):
    buffer = pickle.dumps(args)
    value = socket.htonl(len(buffer))
    size = struct.pack("L", value)
    channel.send(size)
    channel.send(buffer)


def receive(channel):
    size = struct.calcsize("L")
    size = channel.recv(size)
    try:
        size = socket.ntohl(struct.unpack("L", size)[0])
    except struct.error:
        return ''
    buf = ""
    while len(buf) < size:
        buf = channel.recv(size - len(buf))
    return pickle.loads(buf)[0]


class ChatServer(object):
    """ An example chat server using select """

    def __init__(self, port, backlog=5):
        self.clients = 0
        self.clientmap = {}
        self.outputs = []  # list output sockets
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Enable re-using socket address
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((SERVER_HOST, port))
        print("Server listening to port: {} ...".format(port))
        self.server.listen(backlog)
        # Catch keyboard interrupts
        signal.signal(signal.SIGINT, self.sighandler)

    def sighandler(self, signum, frame):
        """ Clean up client outputs """
        # Close the server
        print("Shutting down server...")
        # Close existing client socket
        for output in self.outputs:
            output.close()
        self.server.close()

    def get_client_name(self, client):
        """ Return the name of the client """
        info = self.clientmap[client]
        host, name = info[0][0], info[1]
        return '@'.join((name, host))

    def run(self):
        inputs = [self.server, sys.stdin]
        self.outputs = []
        running = True
        while running:
            try:
                readable, writeable, exceptional =\
                    select.select(inputs, self.outputs, [])
            except select.error:
                break
            for sock in readable:
                if sock == self.server:
                    # Handler the server socket
                    client, address = self.server.accept()
                    print("Chat server: got connection {} from {}"
                          .format(client.fileno(), address))
                    # Read the login name
                    cname = receive(client).split('NAME: ')[1]
                    # Compute client name and send back
                    self.clients += 1
                    send(client, 'CLIENT: ' + str(address[0]))
                    inputs.append(client)
                    self.clientmap[client] = (address, cname)
                    # Send joining information to other clients
                    msg = "\n(connected: New client ({}) from {}"\
                        .format(self.clients, self.get_client_name(client))
                    for output in self.outputs:
                        send(output, msg)
                    self.outputs.append(client)
                elif sock == sys.stdin:
                    # handle standard input
                    junk = sys.stdin.readline()
                    running = False
                else:
                    # handle all other sockets
                    try:
                        data = receive(sock)
                        if data:
                            # Send as new client's message
                            msg = '\n#[' + self.get_client_name(sock) +\
                                ']>>' + data
                            # Send data to all except ourself
                            for output in self.outputs:
                                if output != sock:
                                    send(output, msg)
                        else:
                            print("Chat server: {} hung up"
                                  .format(sock.fineno()))
                            self.clients -= 1
                            sock.close()
                            inputs.remove(sock)
                            # Sending client leaving info to others
                            msg = "\n(Now hung up: Client from %s)"\
                                .format(self.get_client_name(sock))
                            for output in self.outputs:
                                send(output, msg)
                    except socket.error:
                        # Remove
                        inputs.remove(sock)
                        self.outputs.remove(sock)
        self.server.close()


class ChatClient(object):
    """ A commandline chat client using select """

    def __init__(self, name, port, host=SERVER_HOST):
        self.name = name
        self.connected = False
        self.host = host
        self.port = port
        # Initial prompt
        self.prompt = '[' + \
            '@'.join((name, socket.gethostname().split('.')[0])) + ']> '
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, self.port))
            print("Now connected to chat server@port {}".format(self.port))
            self.connected = True
            # send my name ...
            send(self.sock, 'NAME: ' + self.name)
            data = receive(self.sock)
            # contains client address, set it
            addr = data.split('CLIENT: ')[1]
            self.prompt = '[' + '@'.join(((self.name, addr))) + ']> '
        except socket.error:
            print("Failed to connect to chat server @ port {}"
                  .format(self.port))
            sys.exit(1)

    def run(self):
        """ Chat client main loop """
        while self.connected:
            try:
                sys.stdout.write(self.prompt)
                sys.stdout.flush()
                # Wait for input from stdin and socket
                readable, writeable, exceptional = select.select(
                    [0, self.sock], [], [])
                for sock in readable:
                    if sock == 0:
                        data = sys.stdin.readline().strip()
                        if data:
                            send(self.sock, data)
                    elif sock == self.sock:
                        data = receive(self.sock)
                        if not data:
                            print("Client shutting down.")
                            self.connected = False
                        else:
                            sys.stdout.write(data + '\n')
                            sys.stdout.flush()
            except KeyboardInterrupt:
                print("Client interrupted.")
                self.sock.close()
                break

if __name__ == '__main__':
    """
        Example run(foreach terminal):
        Server: python3 2_3_chat_server_with_select --name server --port 1234
        Client1: python3 2_3_chat_server_with_select --name client1 --port 1234
        Client2: python3 2_3_chat_server_with_select --name client2 --port 1234
    """
    parser = argparse.ArgumentParser(
        description='Socket server Example with Select')
    parser.add_argument('--name', action='store', dest='name', required=True)
    parser.add_argument(
        '--port', action='store', dest='port', type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    name = given_args.name
    if name == CHAT_SERVER_NAME:
        server = ChatServer(port)
        server.run()
    else:
        client = ChatClient(name=name, port=port)
        client.run()