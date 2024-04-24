import requests


def emotion_detector(text_to_analyse):
    if not text_to_analyse.strip():  # Check if input is blank
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=myobj, headers=header)

    if response.status_code == 200:
        emotions = response.json()['emotionPredictions'][0]['emotion']
        return {**emotions, 'dominant_emotion': max(emotions, key=emotions.get)}
    elif response.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    else:
        return "Error: Unable to fetch emotions"
