from flask import Flask, jsonify

app = Flask(__name__)


@app.before_request
def before():
    print("This is executed BEFORE each request.")


@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


@app.route('/<int:number>/')
def incrementer(number):
    return "Incrementef number is" + str(number+1)


@app.route('/<string:name>/')
def hello(name):
    return "Hello" + name

# Jsonify for dictionary objects


@app.route('/person/')
def hello():
    return jsonify({'name': 'Jimit', 'address': 'India'})


# Jsonify to automatically serialize lists to JSON response
@app.route('/numbers/')
def print_list():
    return jsonify(list(range(5)))


# return status code
@app.route('/teapot')
def teapot():
    return "Would you like some tea?", 418


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
