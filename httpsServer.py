import BaseHTTPServer, CGIHTTPServer
import ssl

CGIHTTPServer.CGIHTTPRequestHandler.cgi_directories = ["/cgi-bin"]

httpd = BaseHTTPServer.HTTPServer(('localhost', 443), CGIHTTPServer.CGIHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='cert.pem', server_side=True)
sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()
