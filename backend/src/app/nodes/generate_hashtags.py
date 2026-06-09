from app.prompts.generate_hashtags_prompt import generate_hashtags_prompt
from app.schemas.state import LinkedInState
from app.services import get_llm
import json

def generate_hashtags(state: LinkedInState) -> LinkedInState:
    formatted_prompt = generate_hashtags_prompt.format_messages(
        linkedin_post=state["linkedin_post"]
    )
    response = get_llm().with_config({"run_name": "generate_hashtags"}).invoke(formatted_prompt)
    parsed = json.loads(response.content)

    return {"hashtags": parsed.get("hashtags", [])}