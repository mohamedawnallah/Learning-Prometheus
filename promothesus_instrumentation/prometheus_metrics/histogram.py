import time
import http.server
from prometheus_client import start_http_server, Histogram

REQEUEST_RESPOND_TIME = Histogram("app_response_latency_seconds", "Response latency in seconds")

APP_PORT = 8000
METRICS_PORT = 8001

class HandleRequests(http.server.BaseHTTPRequestHandler):

    @REQEUEST_RESPOND_TIME.time()
    def do_GET(self):
        # start_time = time.perf_counter()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First Application</title></head><body style='color: #333; margin-top: 30px;'><center><h2>Welcome to our first Prometheus-Python application.</center></h2></body></html>", "utf-8"))
        self.wfile.close()
        # end_time = time.perf_counter()
        # time_taken = end_time - start_time
        # REQEUEST_RESPOND_TIME.labels("prometheus_python_app", self.command, self.path).observe(time_taken)
        

if __name__ == "__main__":
    start_http_server(METRICS_PORT)
    server = http.server.HTTPServer(('localhost', APP_PORT), HandleRequests)
    server.serve_forever()