
import os 
import json
from flask import Flask
from src import views
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

### swagger specific ###
SWAGGER_URL = '/documentation'
API_URL = ''
swagger_file_dir = os.path.abspath('./files/swagger.json')
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'spec': json.load(open(swagger_file_dir))}
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

app.add_url_rule('/v1/credit_transaction', view_func=views.credit_transaction, methods=['POST'])
