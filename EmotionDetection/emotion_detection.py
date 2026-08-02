import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    hdr = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    bdy = {"raw_document":{"text": text_to_analyze}}  
    emotions = json.loads(requests.post(url,headers = hdr, json = bdy).text)['emotionPredictions'][0]['emotion']
    emotions_dict =  {k: emotions[k] for k in ["anger","disgust","fear","joy","sadness"]}
    emotions_dict["dominant_emotion"] = max(emotions_dict, key=emotions_dict.get)
    return emotions_dict

    





     