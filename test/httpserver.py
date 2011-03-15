from base64 import encodestring
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SimpleHTTPServer import SimpleHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self, *args, **kwargs):
        if (self.path == "/stop"):
            self.send_response(200)
            httpd.socket.close()
        else:
            if not self.path == "/auth":
                self.wfile.write("Response for %s %s" % (self.path, str(self.headers)))
            else:
                if self.headers.getheader('authorization') == ("Basic %s" % encodestring('test:test'))[:-2]:
                    self.wfile.write('worked')
        
            
server_address = ('', 20144)
httpd = HTTPServer(server_address, RequestHandler)
try:
    httpd.serve_forever()
except:
    pass
