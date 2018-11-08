from flask import render_template, request, jsonify

from . import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/chat', methods=["POST"])
def chat():
    message = request.form['messageText']

    greetings = ['hello', 'hi', 'hey', 'yo',
                    'wassup', 'ndeipi', 'how are you']

    exits = ['bye', 'exit', 'go back', 'good bye']


    if message in greetings:
       
        return jsonify({'status': 'OK', 'answer': ''})
    
    elif message in exits:
        return jsonify({'status': 'OK', 'answer': 'Thank you for chatting with me'})
   
    else:
        return jsonify({'status': 'OK', 'answer': "Sorry I didn't understand that"})
