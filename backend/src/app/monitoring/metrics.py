from prometheus_client import Counter,Histogram

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP Requests",
    ["method","endpoint"]
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP Request Duration",
    ["method", "endpoint"]
)

POST_GENERATED = Counter(
    "linkedin_posts_generated_total",   
    "Total AI generated posts"
)

LINKEDIN_PUBLISH_SUCCESS = Counter(
    "linkedin_publish_success_total",
    "Total successful LinkedIn publishes"
)

LINKEDIN_PUBLISH_FAILURE = Counter(
    "linkedin_publish_failure_total",
    "Total failed LinkedIn publishes"
)

AI_ERRORS = Counter(
    "ai_errors_total",
    "Total AI workflow errors"
)