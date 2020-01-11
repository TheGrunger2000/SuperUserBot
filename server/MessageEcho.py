import apiai
import json


class MessageEcho:

    def __init__(self):
        pass

    def run(self, message, token, lang="en", session_id="aibot"):
        assert message is not None
        request = apiai.ApiAI(token).text_request()
        request.lang = lang
        request.session_id = session_id
        request.query = message
        responseJson = json.loads(request.getresponse().read())
        answer = responseJson['result']['fulfillment']['speech']
        return answer
