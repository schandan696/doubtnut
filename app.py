from flask import Flask, request
from datetime import datetime
import persistqueue


app = Flask(__name__)


# the minimal Flask application
@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


@app.route('/schduler', methods=['POST'])
def schdule_json():
    content = request.json
    timestamp = datetime.timestamp(datetime.now())
    content['requestTime'] = timestamp
    ackq = persistqueue.SQLiteAckQueue('data')
    ackq.put(content)
    return str(timestamp)


if __name__ == '__main__':
    app.run(debug=True)
