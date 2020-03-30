import socketserver

class TCPHandler(socketserver.BaseRequestHandler):
    debug = None
    """
    The request handler class for our server.
    """
    def handle(self):
        self.data = self.request.recv(1024).strip()
        if self.debug:
            print(self.data)
        self.request.sendall(self.data.upper())

    @staticmethod
    def set_debug(self, debug=0):
        self.debug = int(debug)
