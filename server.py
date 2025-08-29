import http.server
import socketserver
import os

PORT = 4444

class CORSHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        super().end_headers()

    def guess_type(self, path):
        if path.endswith('.wasm'):
            return 'application/wasm'
        return super().guess_type(path)

# Ensure the current directory is the one where the script is run
# This is important if the script is called from a different directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(("", PORT), CORSHandler) as httpd:
    print(f"Serving at port {PORT} with CORS headers...")
    httpd.serve_forever()
