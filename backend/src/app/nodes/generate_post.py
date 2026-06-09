from src.app.prompts.generate_prompt import generate_prompt
from src.app.schemas.state import LinkedInState
from src.app.services import get_llm
from src.app.monitoring.metrics import POST_GENERATED, AI_ERRORS

def generate_linkedin_post(state:LinkedInState)-> LinkedInState:

    try:
        formatted_prompt = generate_prompt.format_messages(
            the_best_hook=state["the_best_hook"]
        )
        response_linkedin_post = get_llm().with_config({"run_name": "generate_post"}).invoke(formatted_prompt)

        POST_GENERATED.inc()

        return {**state,'linkedin_post':response_linkedin_post.content}
    
    except Exception as e:

        AI_ERRORS.inc()

        print(f"Error in generate_linkedin_post: {e}")

        return {**state,'linkedin_post':"Sorry, I couldn't generate a post at this time."}
