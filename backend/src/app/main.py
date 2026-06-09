from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Removing old import hook

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

from src.app.routes.post_routes import router as post_router
from src.app.routes.auth_routes import router as auth_router

# Include single unified router
app.include_router(post_router)
app.include_router(auth_router)

# def main():

#     graph = app_graph()

#     result = graph.invoke({
#         "topic": "Why Human-in-the-Loop is Important in AI Systems"
#     })

#     linkedin_content = result.get("linkedin_post", "")
#     score = result.get("score", 0)
#     status = result.get("status", "failed")

#     print("*" * 50, f"LinkedIn Post with score : {score} Start", "*" * 50)

#     print("LinkedIn Post:\n", linkedin_content, "\n\n")

#     print("*" * 50, "LinkedIn Post End", "*" * 50)

#     if status == "success":
#         print(f"\n✅ {result.get('message')}")
#         print(f"Post ID: {result.get('linkedin_post_id')}")

#     else:
#         message = result.get("message", "")

#         try:
#             error_data = json.loads(message)
#             print(f"\n❌ Error: {error_data.get('message')}")
#         except Exception:
#             print(f"\n❌ Error: {message}")


# if __name__ == "__main__":
#     main()