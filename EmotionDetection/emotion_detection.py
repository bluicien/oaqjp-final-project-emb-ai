''' This module is for the function that is called to analyze the emotion in a given text.
'''

import json
import requests

def emotion_detector(text_to_analyse) :
    ''' Function that takes a text input parameter and posts it to the watson AI
        for emotion analysis and then receives and returns the response results,
        if results are invalid it passes a 'None' value.
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    my_obj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = my_obj, headers=headers, timeout=5)

    if response.status_code == 400:
        return {"anger": None, 
        "disgust": None, 
        "fear": None, 
        "joy": None, 
        "sadness": None, 
        "dominant_emotion": None 
        }
    
    elif response.status_code == 200:
        resp = json.loads(response.text)
        emotions = resp['emotionPredictions'][0]['emotion']
        dominant_emotion = {'dominant_emotion': (max(emotions, key=emotions.get))}
        emotions.update(dominant_emotion)
        return emotions
    
    # emotion_predictor = json.dumps(emotions)
    # return emotion_predictor
    