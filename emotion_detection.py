import requests
import json

def emotion_detector(text_to_analyze):
    # Define the URL for the Watson Emotion Analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Set the headers required for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Send a POST request to the Watson service
    response = requests.post(url, json=myobj, headers=header)
    
    # Parse the response text into a dictionary
    formatted_response = json.loads(response.text)
    
    return formatted_response
