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
    request.query = message.replace("/bot", "")

    responseJson = json.loads(request.getresponse().read())
    pprint.pprint(responseJson)
    answer_text = responseJson['result']['fulfillment']['speech']
    what = "+".join(message.replace("/bot", "").split(" ")[1:])
    search_data = responseJson['result']['parameters']

    answer = None
    if 'google_search' in search_data:
        if search_data['google_search'] == ['search'] or 'search':
            answer = f'{answer_text}\nhttps://www.google.com/search?q={what}'
    elif 'youtube_search' in search_data:
        if search_data['youtube_search'] == ['video'] or 'video':
            answer = f'{answer_text}\nhttps://www.youtube.com/results?search_query={what}'
    else:
        answer = answer_text
    return answer
