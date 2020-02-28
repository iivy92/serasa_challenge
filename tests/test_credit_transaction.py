import requests
import json
import pytest

def test_compromised_income_true():
    
    url = "http://localhost:5000/v1/credit_transaction"
    headers = {'Content-Type': 'application/json' }
    payload = {
        "transaction": { 
            "id": 1, 
            "consumer_id": 10, 
            "score":500, 
            "income": 400, 
            "requested_value": 10000,
            "installments": 9, 
            "time": "2019-02-13T13:55:00.000Z"
        }
    }
    response = requests.post(url, headers = headers, data = json.dumps(payload))

    assert response.status_code == 202
    assert response.json()["transaction"]["id"] == 1
    assert response.json()["transaction"]["violations"] == ['compromised-income']

def test_low_score_true():
    
    url = "http://localhost:5000/v1/credit_transaction"
    headers = {'Content-Type': 'application/json' }
    payload = {
        "transaction": { 
            "id": 2, 
            "consumer_id": 10, 
            "score":100, 
            "income": 4000, 
            "requested_value": 10000,
            "installments": 9, 
            "time": "2019-02-13T13:55:00.000Z"
        }
    }
    response = requests.post(url, headers = headers, data = json.dumps(payload))

    assert response.status_code == 202
    assert response.json()["transaction"]["id"] == 2
    assert response.json()["transaction"]["violations"] == ["low-score"]

def test_minimum_installments_true():
    
    url = "http://localhost:5000/v1/credit_transaction"
    headers = {'Content-Type': 'application/json' }
    payload = {
        "transaction": { 
            "id": 3, 
            "consumer_id": 10, 
            "score":600, 
            "income": 4000, 
            "requested_value": 1000,
            "installments": 1, 
            "time": "2019-02-13T13:55:00.000Z"
        }
    }
    response = requests.post(url, headers = headers, data = json.dumps(payload))

    assert response.status_code == 202
    assert response.json()["transaction"]["id"] == 3
    assert response.json()["transaction"]["violations"] == ["minimum-installments"]

def test_doubled_transaction_true():
    
    url = "http://localhost:5000/v1/credit_transaction"
    headers = {'Content-Type': 'application/json' }
    payload = {
        "transaction": { 
            "id": 3, 
            "consumer_id": 10, 
            "score":600, 
            "income": 4000, 
            "requested_value": 10000,
            "installments": 12, 
            "time": "2019-02-13T13:55:00.000Z"
        }
    }
    response = requests.post(url, headers = headers, data = json.dumps(payload))

    assert response.status_code == 202
    assert response.json()["transaction"]["id"] == 3
    assert response.json()["transaction"]["violations"] == ["doubled-transactions"]





    
 