import socketserver
import sys

# Debug statement. Script can be started with
# "python server.py 0"
# "python server.py 1"
if int(sys.argv[1]) == 1:
    debug = 1
else:
    debug = 0

print("Debug: ", debug)
HOST, PORT = "", 9999

class TCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.
    """
    def handle(self):
        self.data = self.request.recv(1024).strip()
        if debug:
            print(self.data)
        self.request.sendall(self.data.upper())


server = socketserver.TCPServer((HOST, PORT), TCPHandler)

# run server
server.serve_forever()