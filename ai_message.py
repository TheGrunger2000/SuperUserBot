from os import environ

from dialogflow_v2 import SessionsClient
from dialogflow_v2.types import TextInput, QueryInput
from google.protobuf.json_format import MessageToDict

from auth import get_setting

environ['GOOGLE_APPLICATION_CREDENTIALS'] = get_setting(
    'API Keys', 'google_private_key_path')
PROJECT_ID = get_setting('API Keys', 'dialogflow_project_id')


def get_response(text, session_id='aibot', language_code='ru'):
    session_client = SessionsClient()
    session = session_client.session_path(PROJECT_ID, session_id)

    if text:
        text_input = TextInput(
            text=text, language_code=language_code)
        query_input = QueryInput(text=text_input)
        response = session_client.detect_intent(
            session=session, query_input=query_input)

        return MessageToDict(response.query_result)
    raise ValueError('message cannot be empty')


def action_check(response):
    action_dict = {'google_search': google_search,
                   'youtube_search': youtube_search,
                   'audio_search': audio_search,
                   'gif_search': gif_search}
    action = response.get('action')
    parameters = response.get('parameters')
    answer_message = response.get('fulfillmentText')
    search_answer = None
    if action:
        if parameters:
            search_string = parameters.get('any')
            if search_string:
                search_answer = action_dict[action](search_string)
    return answer_message, search_answer


def ai_message(message):
    answer_mesage, search_answer = action_check(get_response(message))
    return f'{answer_mesage}\n{search_answer}'


def google_search(what):
    return 'Found'


def youtube_search(what):
    return 'Found'


def audio_search(what):
    return


def gif_search(what):
    return 'Found'


TEST_MESSAGES = ['Найди гифку запрос', 'Найди музыку запрос',
                 'Найди в ютубе запрос', 'Найди в гугле запрос', 'Привет', 'вльвву']
for msg in TEST_MESSAGES:
    print(ai_message(msg))
