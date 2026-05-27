import http.server, os, sys
os.chdir("/Users/michalpodskoc/Desktop/portfolio-michalpodskoc")
httpd = http.server.HTTPServer(("", 3333), http.server.SimpleHTTPRequestHandler)
print("Serving on http://localhost:3333", flush=True)
httpd.serve_forever()
