
from flask import Flask

from flask_pymongo import PyMongo

from bson.json_util import dumps

from flask import jsonify, request

from datetime import datetime

from dateutil.relativedelta import relativedelta

from env.task import random_with_N_digits

app = Flask(__name__)

app.secret_key = "secretkey"

app.config['MONGO_URI'] = "mongodb://localhost:27017/deepak"

mongo = PyMongo(app)

@app.route('/api/v1/activate', methods=['GET', 'POST'])
def senddetails():
    try:
         _json = request.json
         _debit_card_id = _json['debit card id']
         _customerid = _json['customer id']

         #debit card number is should be 16 digit with starting  1234
         _debit_card_no = "1234" + str(random_with_N_digits(12))

          # random cvv generated
         _cvv = random_with_N_digits(3)
         _start_date = datetime.utcnow().strftime('%Y-%m-%d ')
         _expiry_date = datetime.now() + relativedelta(years=20 , days=0)

         if request.method == 'POST':
              id1 = mongo.db.debit.insert_one(
                 {'debit card id': _debit_card_id, 'customer id': _customerid, '_starting_date': _start_date ,'_expiry_date' : _expiry_date , 'cvv' : _cvv ,'debit_card_no' :  _debit_card_no })

              print(id)

              resp = jsonify("user added successfully")

              resp.status_code = 200

              return resp

         else:

             return "missing aarguments"

    except Exception as e:
           return (str(e))


@app.route('/api/v1/active')
def user():
    try:
        user = mongo.db.debit.find()
        resp = dumps(user)
        print(resp)
        return resp
    except Exception as e:
        return (str(e))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005, debug=True)


