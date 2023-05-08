import time
import http.server
from prometheus_client import start_http_server, Gauge

REQUEST_INPROGRESS = Gauge("app_requests_inprogress", "requests in progress", ["app_name", "method", "endpoint"])
REQUEST_LAST_SERVED = Gauge("app_requests_last_served", "last request served")

APP_PORT = 8000
METRICS_PORT = 8001

class HandleRequests(http.server.BaseHTTPRequestHandler):

    @REQUEST_INPROGRESS.track_inprogress(labels=("prometheus_python_app", "GET", "/"))
    def do_GET(self):
        # REQUEST_INPROGRESS.labels("prometheus_python_app", self.command, self.path).inc()
        time.sleep(5)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First Application</title></head><body style='color: #333; margin-top: 30px;'><center><h2>Welcome to our first Prometheus-Python application.</center></h2></body></html>", "utf-8"))
        self.wfile.close()
        REQUEST_LAST_SERVED.set(time.time())
        # REQUEST_INPROGRESS.labels("prometheus_python_app", self.command, self.path).dec()

if __name__ == "__main__":
    start_http_server(METRICS_PORT)
    server = http.server.HTTPServer(('localhost', APP_PORT), HandleRequests)
    server.serve_forever()