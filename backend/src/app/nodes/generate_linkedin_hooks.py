from app.prompts.linkedin_hooks_prompt import linkedin_hooks_prompt
from app.schemas.state import LinkedInState
from app.services import get_llm
import json

def generate_linkedin_hooks(state:LinkedInState)-> LinkedInState:

    
    formatted_prompt = linkedin_hooks_prompt.format_messages(
        topic=state["topic"]
    )

    response = get_llm().with_config({"run_name": "generate_hooks"}).invoke(formatted_prompt)
    content = response.content

    try:
        parsed_hooks = json.loads(content)
        hooks = parsed_hooks.get("hooks", [])
    except Exception:
        hooks = []

    return {
        "hooks": hooks
    }