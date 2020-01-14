# -*- coding: utf-8 -*-
import apiai
import json
import pprint


TOKEN = "TOKEN"


def ai_message(message, lang="ru", session_id="aibot"):
    assert message is not None
    request = apiai.ApiAI(TOKEN).text_request()
    request.lang = lang
    request.session_id = session_id
    request.query = message.replace("/d" or "/bot", "")

    responseJson = json.loads(request.getresponse().read())
    pprint.pprint(responseJson)
    answer_text = responseJson['result']['fulfillment']['speech']
    what = "+".join(message.replace("/d" or "/bot", "").split(" ")[1:])

    search_data = responseJson['result']['parameters']

    if search_data['google_search'] == ['search']:
        answer = f'{answer_text}\nhttps://www.google.com/search?ei=Qb8cXqeHHdD76QTxqZHABw&q={what}'
    elif search_data['youtube_search'] == ['video']:
        answer = f"https://www.youtube.com/results?search_query={what}"
    else:
        answer = answer_text
    return answer
