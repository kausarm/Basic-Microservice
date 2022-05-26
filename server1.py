from flask import Flask, jsonify
import mysql.connector


app = Flask(__name__)

@app.route('/kausar/getDataBarang', methods=['GET'])
def get_data():

    conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='ecommerce')

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM barang")

    data = cursor.fetchall()
    hasil = jsonify({'data': data})

    return hasil

    conn.close()

if __name__ == '__main__':
    app.run(debug=True,port="9000")