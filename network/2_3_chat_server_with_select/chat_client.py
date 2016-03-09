import socket
import sys
import select
import connect_util


class ChatClient(object):
    """ A commandline chat client using select """

    def __init__(self, name, port, host=connect_util.SERVER_HOST):
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
            connect_util.send(self.sock, 'NAME: ' + self.name)
            data = connect_util.receive(self.sock)
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
                            connect_util.send(self.sock, data)
                    elif sock == self.sock:
                        data = connect_util.receive(self.sock)
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
