from flask import jsonify
from flask import request
from src.models.model import credit_transactions
import json
import http

def __init__(self):
    self.credit_transaction()

def credit_transaction():
    data = request.get_json()
    try:
        output = credit_transactions.transport_trasaction(data)
        credit_transactions.save_transaction(data)
        return jsonify({"transaction": output}), http.HTTPStatus.ACCEPTED
    except Exception as e:
        return jsonify({'msg': "Error", 'AdditionalData': str(e)}), http.HTTPStatus.BAD_REQUEST
