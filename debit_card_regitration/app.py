from  flask import Flask

from flask_pymongo import PyMongo

from flask import jsonify,request

from datetime import datetime

import requests


app = Flask(__name__)

app.secret_key = "secretkey"

app.config['MONGO_URI'] = "mongodb://localhost:27017/debit"

mongo = PyMongo(app)

@app.route('/add', methods=['POST'])

# This add admin function is used to add the debit_card_details and customerid and date_time to database

def add_admin():
    try:
        _json = request.json
        _debit_card_id = _json['debit card id']
        _customerid = _json['customer id']
        today = datetime.utcnow().strftime('%Y-%m-%d ')


        if request.method == 'POST':
            api_url = "http://192.168.0.104:5002/api/v1/debit"
            data = {'debit card id': _debit_card_id, 'customer id': _customerid}
            requests.post(url=api_url, json=data)

            id = mongo.db.debit.insert_one({'debit card id': _debit_card_id, 'customer id': _customerid, 'date_and_time': today})

            print(id)

            resp = jsonify("user added successfully")

            resp.status_code = 200

            return resp

        else:
            return "missing aarguments"

    except Exception as e:
               return(str(e))

# this function is used to get the details of the customer
@app.route('/api/v1/debitreceive', methods=['GET'])
def fin2_user():
    try:
        api_url = requests.get("http://192.168.0.104:5002/api/v1/active1")

        result = api_url.json()

        print (result)

        return "result"

    except Exception as e:
            return (str(e))

# This function is used to get the adhar and pancard image of the customer
@app.route('/add1', methods=['POST'])
def upload():
    try:
        adhar_card = request.files['adhar_card']
        adhar_card.save('E:\pic\Adhar.png')
        pan_card = request.files['pan_card']
        pan_card.save('E:\pic\pancard.png')

        return "ok"
    except Exception as e:
            return(str(e))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004, debug=True)


