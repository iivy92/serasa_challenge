from flask import jsonify
from flask import request
from src.models.model import CreditTransactions
import json
import http


def __init__(self):
    self.ct = CreditTransactions()

def credit_transaction():
    data = request.get_json()
    try:
        output = self.ct.transport_trasaction(data)
        return jsonnify({"transaction": output}), http.HTTPStatus.ok
    except Exception as e:
        return jsonify({'msg': "Error", 'AdditionalData': str(e)}), http.HTTPStatus.BAD_REQUEST
