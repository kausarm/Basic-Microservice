from flask import Flask, jsonify
import requests


app = Flask(__name__)

@app.route('/gateAway/getBarang', methods=['GET'])
def get_data():
    url = 'http://127.0.0.1:9000/kausar/getDataBarang'
    response = requests.request('GET', url)
    return response.text

@app.route('/gateAway/getTingkatPrevalensiStunting', methods=['GET'])
def method_name():
    url = 'http://127.0.0.1:3000/kausar/getTingkatPrevalensiStunting'
    res = requests.request('GET', url)

    return res.text


if __name__ == '__main__':
    app.run(debug=True,port="8000")