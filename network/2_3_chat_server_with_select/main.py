#!/usr/bin/python3
import connect_util
from chat_server import ChatServer
from chat_client import ChatClient
import argparse


if __name__ == '__main__':
    """
        Example (foreach terminal):
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
    if name == connect_util.CHAT_SERVER_NAME:
        server = ChatServer(port)
        server.run()
    else:
        client = ChatClient(name=name, port=port)
        client.run()
