from contextlib import redirect_stdout
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def destroy():
    if 'data' in request.form:
        data = request.form['data']

        with open('/dev/null', 'w') as f:
            with redirect_stdout(f):
                print(data)
        
        return {
            'status': '200',
            'message': 'Thank you for using connor.fu\nn!'
        }
    else:
        return {
            'status': '400',
            'message': 'Your data was improperly formatted.  Please send all data to the \'data\' field.'
        }

print('success!')