import socket
import click

@click.command()
@click.option('--host', '-h', help='QOTD server IP address.', required=True)
@click.option('--port', '-p', help='QOTD server port.', required=True, type=int)
def main(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    s.sendall(b'')
    s.shutdown(socket.SHUT_WR)
    while True:
        data = s.recv(4096)
        if not data:
            break
        print(repr(data))
    s.close()

if __name__ == '__main__':
    main()