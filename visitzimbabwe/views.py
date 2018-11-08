from flask import render_template, request, jsonify

from . import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/chat', methods=["POST"])
def chat():
    message = request.form['messageText']

    greetings = ['hello', 'hi','hie', 'hey', 'yo',
                    'wassup', 'ndeipi', 'how are you']

    exits = ['bye', 'exit', 'go back', 'good bye','thanks','thank you']


    if message in greetings:
        response = ''
        return jsonify({'status': 'OK', 'answer': response})
    
    elif message in exits:
        return jsonify({'status': 'OK', 'answer': 'Thank you for chatting with me'})
   
    else:
        return jsonify({'status': 'OK', 'answer': "Sorry I didn't understand that"})
