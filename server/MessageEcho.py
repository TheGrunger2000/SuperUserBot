import apiai
import json


class MessageEcho:

    def __init__(self):
        pass

    def run(self, mesage, token, lang="en", session_id="aibot"):
        assert mesage != None
        request = apiai.ApiAI(token).text_request()
        request.lang = lang
        request.session_id = session_id
        request.query = mesage
        responseJson = json.loads(request.getresponse().read())
        answer = responseJson['result']['fulfillment']['speech']
        return answer
