# app.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        if parsed_path.path == "/test":
            query = urllib.parse.parse_qs(parsed_path.query)
            redirect_url = query.get("redirect", [""])[0]

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            # Aquí simula que inserta directamente el parámetro sin sanear
            response = f"""
                <html>
                <head><title>XSS Test</title></head>
                <body>
                    <p>Redirigiendo a: {redirect_url}</p>
                    <script>
                        document.write("Parámetro recibido: " + decodeURIComponent("{urllib.parse.quote(redirect_url)}"));
                    </script>
                </body>
                </html>
            """
            self.wfile.write(response.encode())
        else:
            self.send_error(404, "File not found.")

# Inicia el servidor
def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print("Servidor corriendo en http://localhost:8000")
    httpd.serve_forever()

if __name__ == '__main__':
    run()


