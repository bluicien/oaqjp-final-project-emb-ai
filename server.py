''' Module to start up the Flask server for the emotion detection app.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def get_emotion() :
    ''' Gets the client input and passes it to the emotion analyzer function.
    Receives the response and passes it to the browser to display to the client.
    Also manages the error message for invalid input.
    '''
    text_to_analyse = request.args.get('textToAnalyze')
    emotion = emotion_detector(text_to_analyse)

    if emotion['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is 'anger': {emotion['anger']},\
    'disgust': {emotion['disgust']}, 'fear': {emotion['fear']}, 'joy': {emotion['joy']} and \
    'sadness': {emotion['sadness']}. The dominant emotion is \
    <b>{emotion['dominant_emotion']}</b>"

@app.route('/')
def index_page() :
    ''' Renders the index page for client input
    '''

    return render_template('index.html')

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
