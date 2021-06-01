from  flask import Flask

from flask_pymongo import PyMongo

from flask import jsonify,request

import requests



app = Flask(__name__)

app.secret_key = "secretkey"

app.config['MONGO_URI'] = "mongodb://localhost:27017/admin"

mongo = PyMongo(app)



# this function is used to get the data from card activation service
@app.route('/api/v1/debit', methods = ['GET', 'POST'])
def req2():
    try:
        # _json = request.json
        _debit_card_id = request.json['debit card id']
        _customerid = request.json['customer id']

        api_url = "http://192.168.0.104:5005/api/v1/activate"

        data = {'debit card id': _debit_card_id, 'customer id': _customerid}

        txn = requests.post(url=api_url, json=data)

        return "success"
    except Exception as e:
          return (str(e))


# this function is used to get the card details
@app.route('/api/v1/active1' , methods = ['GET'])
def find3_user():
    try:
        api_url = requests.get("http://192.168.0.104:5005/api/v1/active")

        result = api_url.json()

        print (result)

        return "result"
    except Exception as e:
            return (str(e))



if __name__ == "__main__":
   app.run(host='0.0.0.0',port=5002)
