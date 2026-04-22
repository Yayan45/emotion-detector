def emotion_detector(text):
    emotions = {
        "anger": 0.1,
        "joy": 0.7,
        "sadness": 0.1,
        "fear": 0.05,
        "disgust": 0.05
    }
    dominant = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "fear": emotions["fear"],
        "disgust": emotions["disgust"],
        "dominant_emotion": dominant
    }