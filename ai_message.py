# -*- coding: utf-8 -*-
import apiai
import json
import pprint


TOKEN = "1d10485eceee4565a2e2f51a4922e971"


def ai_message(message, lang="ru", session_id="aibot"):
    assert message is not None
    request = apiai.ApiAI(TOKEN).text_request()
    request.lang = lang
    request.session_id = session_id
    request.query = message.replace("/d", "")
    responseJson = json.loads(request.getresponse().read())
    pprint.pprint(responseJson)
    answer_text = responseJson['result']['fulfillment']['speech']
    what = "+".join(message.replace("/d", "").split(" ")[1:])
    if responseJson['result']['metadata']['intentName'] == 'google.search':
        answer = f'{answer_text}\nhttps://www.google.com/search?ei=Qb8cXqeHHdD76QTxqZHABw&q={what}'
    elif responseJson['result']['metadata']['intentName'] == 'youtube.search':
        answer = f"https://www.youtube.com/results?search_query={what}"
    else:
        answer = answer_text
    return answer
