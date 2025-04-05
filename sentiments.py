import json
from transformers import pipeline

# Load the emotion classification model
emotion_classifier = pipeline('text-classification', model='bhadresh-savani/distilbert-base-uncased-emotion')

# Example summarized transcript from a meeting
meeting_summary = """
In today's meeting, the team discussed the upcoming product launch and the marketing strategies involved. 
There was a consensus on the timeline, but some concerns were raised about the budget allocation and the resource distribution. 
Everyone agreed that more discussion is needed to finalize the advertising channels. The team expressed excitement about the new features 
being introduced, although there were apprehensions about potential customer feedback and support issues post-launch.
"""

def sentiments(text):
    # Prepare the results dictionary
    results = {
        "overall_emotion": {},
        "sentence_emotions": []
    }
    
    # Analyze the overall emotion of the meeting summary
    overall_result = emotion_classifier(text)
    results["overall_emotion"] = {
        "label": overall_result[0]['label'],
        "score": overall_result[0]['score']
    }
    
    # Analyze emotion by sentence
    sentences = text.split('. ')  # Simple sentence splitter
    for sentence in sentences:
        if sentence.strip():
            sentence_result = emotion_classifier(sentence)
            results["sentence_emotions"].append({
                "sentence": sentence,
                "emotion": {
                    "label": sentence_result[0]['label'],
                    "score": sentence_result[0]['score']
                }
            })

    # Convert results to JSON
    json_results = json.dumps(results)
    print(json_results)
    return json_results

# Call the function with the summarized transcript
sentiments(meeting_summary)
