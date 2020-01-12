import apiai
import json


TOKEN = "1d10485eceee4565a2e2f51a4922e971"


def random_message(message, lang="en", session_id="aibot"):
    assert message is not None
    request = apiai.ApiAI(TOKEN).text_request()
    request.lang = lang
    request.session_id = session_id
    request.query = message
    responseJson = json.loads(request.getresponse().read())
    answer = responseJson['result']['fulfillment']['speech']
    return answer
