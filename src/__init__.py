
from flask import Flask
from src import views

app = Flask(__name__)

app.add_url_rule('/v1/credit_transaction', view_func=views.credit_transaction, methods=['POST'])
