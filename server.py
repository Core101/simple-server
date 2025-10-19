import http.server
import socketserver

# Define the port the server will run on
PORT = 8000
# Define the handler (simple HTTP request handler)
Handler = http.server.SimpleHTTPRequestHandler

# Set up the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    print(f"Access it in your browser at: http://localhost:{PORT}")
    
    # Start the server and keep it running indefinitely
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        # Graceful shutdown when Ctrl+C is pressed
        print("\nServer stopped.")
        httpd.shutdown()

# The server will automatically stop serving when the 'with' block is exited,
# though 'serve_forever' usually prevents this until an interrupt occurs.
