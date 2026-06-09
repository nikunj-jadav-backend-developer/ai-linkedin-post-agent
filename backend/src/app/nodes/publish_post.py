from app.schemas.state import LinkedInState
from app.services import post_to_linkedin_api
import requests

def post_linkedin_after_approve(state: LinkedInState) -> LinkedInState:
        
        linkedin_post = state["linkedin_post"]
        hashtags = state.get("hashtags")
        linkedin_token = state.get("linkedin_token")
        linkedin_person_id = state.get("linkedin_person_id")
        
        if not linkedin_token or not linkedin_person_id:
            return {
                "status": "failed",
                "message": "Missing LinkedIn authentication tokens"
            }
        
        result = post_to_linkedin_api(linkedin_post, access_token=linkedin_token, person_id=linkedin_person_id, hashtags=hashtags)

        try:

            if result.status_code in [200, 201, 202]:
                data = result.json()
                post_id = data.get("id")

                return {
                    "status": "success",
                    "message": "Post successfully published to LinkedIn",
                    "linkedin_post_id": post_id
                }
            else:
                return {
                    "status": "failed",
                    "message": result.text,
                    "status_code": result.status_code
                }

        except requests.exceptions.Timeout:
            return {
                "status": "failed",
                "message": "Request timed out"
            }

        except requests.exceptions.RequestException as e:
            return {
                "status": "failed",
                "message": str(e)
            }