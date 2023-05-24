from socketserver import StreamRequestHandler, TCPServer


class Handler(StreamRequestHandler):
    def handle(self):
        while True:
            data = self.rfile.readline()
            if not data:
                break

            print('receive', data)
            self.wfile.write(data.upper())

        print('client close')


server = TCPServer(('127.0.0.1', 8881), Handler)
server.serve_forever()
