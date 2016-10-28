from http.server import HTTPServer, BaseHTTPRequestHandler, HTTPStatus


class HttpHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET")
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(b"""<h1>Hello world</h1>
        <form method='post'><input type='text' name='name' /><button type='submit'>Send</button>""")

    def do_POST(self):
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        content_length = int(self.headers["Content-length"])
        body = self.rfile.read(content_length).decode("utf-8")
        form = {}
        for kv in body.split("&"):
            k, v = kv.split("=")
            form[k] = v
        self.wfile.write(bytes("Hello {}".format(form["name"]), "utf-8"))

def main():
    address = ("localhost", 8000)
    server = HTTPServer(address, HttpHandler)
    server.serve_forever()

if __name__ == "__main__":
    print("Open the browser http://localhost:8000")
    main()