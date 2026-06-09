from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from src.app.monitoring.metrics import REQUEST_COUNT
from src.app.monitoring.middleware import PrometheusMiddleware
from src.app.routes.post_routes import router as post_router
from src.app.routes.auth_routes import router as auth_router

app = FastAPI(
    title="LinkedIn Content Automation API",
    description="AI-powered LinkedIn content generation, evaluation, and publishing system",
    version="1.0.0"
)

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ai-linkedin-post-agent.vercel.app",
        "http://localhost:5173",
    ],
    allow_origin_regex=r"https://.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_middleware(PrometheusMiddleware)


app.include_router(post_router)
app.include_router(auth_router)

@app.get("/metrics",tags=["Monitoring"],include_in_schema=True)
def metrics():
    return Response(
        generate_latest(),
        media_type=CONTENT_TYPE_LATEST
    )

@app.get("/test")
def test():

    REQUEST_COUNT.labels(
        "GET",
        "/test"
    ).inc()

    return {"status": "ok"}