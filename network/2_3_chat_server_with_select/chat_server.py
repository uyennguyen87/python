import signal
import socket
import select
import sys
import connect_util


class ChatServer(object):
    """ An example chat server using select """

    def __init__(self, port, backlog=5):
        self.clients = 0
        self.clientmap = {}
        self.outputs = []  # list output sockets
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Enable re-using socket address
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((connect_util.SERVER_HOST, port))
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

    def _handle_socket_server(self, inputs):
        client, address = self.server.accept()
        print("Chat server: got connection {} from {}"
              .format(client.fileno(), address))
        # Read the login name
        cname = connect_util.receive(client).split('NAME: ')[1]
        # Compute client name and send back
        self.clients += 1
        connect_util.send(client, 'CLIENT: ' + str(address[0]))
        inputs.append(client)
        self.clientmap[client] = (address, cname)
        # Send joining information to other clients
        msg = "\n(connected: New client ({}) from {}"\
            .format(self.clients, self.get_client_name(client))
        for output in self.outputs:
            connect_util.send(output, msg)
        self.outputs.append(client)

    def _handle_all_other_sockets(self, sock, inputs):
        try:
            data = connect_util.receive(sock)
            if data:
                # Send as new client's message
                msg = '\n#[' + self.get_client_name(sock) +\
                    ']>>' + data
                # Send data to all except ourself
                for output in self.outputs:
                    if output != sock:
                        connect_util.send(output, msg)
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
                    connect_util.send(output, msg)
        except socket.error:
            # Remove
            inputs.remove(sock)
            self.outputs.remove(sock)

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
                    self._handle_socket_server(inputs)
                elif sock == sys.stdin:
                    # handle standard input
                    junk = sys.stdin.readline()
                    running = False
                else:
                    self._handle_all_other_sockets(sock, inputs)
        self.server.close()

