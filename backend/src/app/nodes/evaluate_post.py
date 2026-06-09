from app.prompts.evaluate_prompt import evaluate_prompt
from app.schemas.state import LinkedInState
from app.services import get_llm
import json

def evaluate_linkedin_post(state:LinkedInState)-> LinkedInState:

    
    formatted_prompt = evaluate_prompt.format_messages(
        linkedin_post= state["linkedin_post"]
    )
    response = get_llm().with_config({"run_name": "evaluate_post"}).invoke(formatted_prompt)
    parsed = json.loads(response.content)

    return { 'linkedin_post':parsed["linkedin_post"],'score':parsed["score"],'feedback':parsed["feedback"] }