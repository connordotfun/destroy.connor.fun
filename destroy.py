from contextlib import redirect_stdout
from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/', methods=['POST'])
def destroy():
    data = request.data
    if data:
        with open('/dev/null', 'w') as f:
            with redirect_stdout(f):
                print(data)
        
        return Response("Thank you for using destroy.connor.fu !\nn", status=200)

    else:
        return Response("Your data was improperly formatted.  Please send all data in the post body.", status=400)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)