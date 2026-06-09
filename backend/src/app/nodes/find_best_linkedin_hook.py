from app.schemas.state import LinkedInState
from app.schemas.schema import HooksResponse
from langchain_core.output_parsers import PydanticOutputParser


def find_best_linkedin_hook(state: LinkedInState) -> LinkedInState:

    hooks = state.get("hooks", [])

    if not hooks:
        return {
            "the_best_hook": "",
            "score": 0
        }

    # Use max() with a key that handles dictionary access safely
    best_hook_obj = max(
        hooks,
        key=lambda x: (x.get("score", 0), len(x.get("hook", "")))
    )

    return {
        "the_best_hook": best_hook_obj.get("hook", ""),
        "score": best_hook_obj.get("score", 0)
    }