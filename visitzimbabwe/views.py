from flask import render_template, request, jsonify

from . import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/brand')
def brand():
    return render_template('brand.html')

@app.route('/market')
def market():
    return render_template('last.html')



@app.route('/chat', methods=["POST"])
def chat():
    data = request.get_json()
    message = data['messageText'] 

    greetings = ['hello', 'hi','hie', 'hey', 'yo',
                    'wassup', 'ndeipi', 'how are you']

    exits = ['bye', 'exit', 'go back', 'good bye','thanks','thank you']


    if message in greetings:
        response = "Hi there, which place would you like to visit? <br/><br/><a href='' target='_blank'><button  style='background-color: #0080FF' class='btn btn-primary btn-block btn-round'>Kariba</button></a><br/>" + \
                    "<a href='' target='_blank'><button  style='background-color: #0080FF' class='btn btn-primary btn-block btn-round'>Victoria Falls</button></a><br/><a href='' target='_blank'><button  style='background-color: #0080FF' class='btn btn-primary btn-block btn-round'>Bvumba</button></a></button>"
        return jsonify({'status': 'OK', 'answer': response})
    
    elif message in exits:
        return jsonify({'status': 'OK', 'answer': 'Thank you for chatting with me'})
   
    else:
        return jsonify({'status': 'OK', 'answer': "Sorry I didn't understand that"})
