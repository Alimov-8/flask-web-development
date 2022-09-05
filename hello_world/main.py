from flask import Flask, request


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['POST'])
def api():
    if not request.is_json:
        return "Missing JSON request", 400

    data = request.json.get('data', None)    
    return data


if __name__ == '__main__':
    app.run()
