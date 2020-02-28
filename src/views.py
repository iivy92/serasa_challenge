from flask import jsonify
from flask import request
from src.models.model import credit_transactions
from src.utils.logger import logger
import json
import http

def __init__(self):
    self.credit_transaction()

def credit_transaction():
    data = request.get_json()
    try:
        logger.info(f'Trying to authorize transaction for consumer: {data["transaction"]["id"]}')
        output = credit_transactions.transport_trasaction(data)
        credit_transactions.save_transaction(data)
        logger.info(f'Transaction processed for consumer: {data["transaction"]["id"]}')
        return jsonify({"transaction": output}), http.HTTPStatus.ACCEPTED
    except Exception as e:
        logger.info(f'Something bad happened with the transaction. Error: {repr(e)}')
        return jsonify({'msg': "Error", 'AdditionalData': repr(e)}), http.HTTPStatus.BAD_REQUEST
