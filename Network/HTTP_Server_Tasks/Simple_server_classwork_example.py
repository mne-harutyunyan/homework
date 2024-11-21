from http.server import BaseHTTPRequestHandler, HTTPServer
import json
users = []
class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type','text/html')
        self.end_headers()
        self.wfile.write(b'''
                         <body>
                         <button> Click me </button>
                         </body>
                         ''')
    def do_POST(self):
        self.content_length=int(self.headers['Content-Length'])
        result = self.rfile.read(self.content_length)
        print(result)
        user_data = json.loads(result)
        users.append(user_data)
        self.send_response(201)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response = {"Data successfully added": user_data}
        self.wfile.write(json.dumps(response).encode('utf-8'))



def run(server_class = HTTPServer,handler_class = SimpleRequestHandler,port=8000):
    server_address = ('127.0.0.1', port)
    httpd = server_class(server_address,handler_class)
    print(f'server is running at port: {port}')
    httpd.serve_forever()

run()