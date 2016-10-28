from http.server import HTTPServer, BaseHTTPRequestHandler


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET")
        # заголовки запроса
        #print(self.headers)

        self.send_response(200) # Ok
        self.send_header("Content-type", "text/html")
        self.end_headers()

        #self.wfile.write(b"<h1>Hello Web</h1>")
        #self.wfile.write(bytes("<p>Это рабочий сервер</p>", "utf-8"))
        with open("index.html", "rb") as html:
            self.wfile.write(html.read())

    def do_POST(self):
        print("POST")
        # заголовки запроса
        #print(self.headers)

        self.send_response(200)  # Ok
        self.send_header("Content-type", "text/html")
        self.end_headers()

        content_length = int(self.headers["Content-Length"])
        content = self.rfile.read(content_length).decode("utf-8")
        print(content)
        form = {}
        for field in content.split("&"):
            k, v = field.split("=")
            form[k] = v
        if form['login'] == "admin" and form['password'] == "qwerty":
            self.wfile.write(b"<h1>Welcome admin</h1>")
        else:
            self.wfile.write(b"<h1>Go away</h1>")


address = ("localhost", 8080)
httpd = HTTPServer(address, HttpHandler) # настройка сервера
httpd.serve_forever() # запуск сервера