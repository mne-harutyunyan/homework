from http.server import BaseHTTPRequestHandler, HTTPServer
import json
any_info = []
class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type','text/html')
        self.end_headers()
        self.wfile.write(b'''
                         GET request recieved!
                         ''')
    def do_POST(self):
        self.content_length=int(self.headers['Content-Length'])
        result = self.rfile.read(self.content_length)
        print(result)
        any_data = json.loads(result)
        any_info.append(any_data)
        self.send_response(201)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response = {"POST request received!": any_data}
        self.wfile.write(json.dumps(response).encode('utf-8'))



def run(server_class = HTTPServer,handler_class = SimpleRequestHandler,port=8000):
    server_address = ('127.0.0.1', port)
    httpd = server_class(server_address,handler_class)
    print(f'server is running at port: {port}')
    httpd.serve_forever()
    
if __name__ == "__main__":
    run()