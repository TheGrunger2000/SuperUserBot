from auth import get_setting
import dialogflow_v2 as dialogflow
import os
import pprint
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = get_setting(
    "API Keys", "google_private_key_path")
PROJECT_ID = get_setting("API Keys", "dialogflow_project_id")


def get_response(text, session_id="aibot", language_code="ru"):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(PROJECT_ID, session_id)

    if text:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(
            session=session, query_input=query_input)

        return response
    else:
        raise ValueError("message cannot be empty")


def message_check(response):
    answer = response.query_result.fulfillment_text
    if response.query_result.parameters.fields.get("google"):
        what = response.query_result.parameters.fields['any'].string_value.replace(
            " ", "+")
        answer = f'{answer}\nhttps://www.google.com/search?q={what}'
    return answer


def ai_message(message):
    return message_check(get_response(message))
