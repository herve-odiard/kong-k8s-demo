from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def status():
    return jsonify({'status': 'ok', 'version': '1.1.0' })

if __name__ == '__main__':
    app.run()
