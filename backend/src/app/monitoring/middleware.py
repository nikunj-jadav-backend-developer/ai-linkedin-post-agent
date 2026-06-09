import time
from starlette.middleware.base import BaseHTTPMiddleware
from src.app.monitoring.metrics import ( REQUEST_LATENCY , REQUEST_COUNT )

class PrometheusMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):

        start_time = time.time()

        response = await call_next(request)

        end_time = time.time()

        duration = end_time - start_time

        REQUEST_COUNT.labels(method = request.method, endpoint = request.url.path).inc()
        REQUEST_LATENCY.labels(method = request.method, endpoint = request.url.path).observe(duration)

        return response