import socketserver
from server import TCPHandler

if __name__ == '__main__':
    server = socketserver.TCPServer(("", 9999), TCPHandler)

    # run server
    server.serve_forever()