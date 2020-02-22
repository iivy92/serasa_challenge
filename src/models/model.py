import json

class CreditTransaction():

    def __init__(self):
        self.
    
    def trasaction(self, data):
        data = json.loads(data)

    #TODO: put values in constants folder
    def _income_validation(self,data):
        quota = int(data["transaction"]["requested_value"]) / int(data["transaction"]["installments"])
        committed_income = int(data["transaction"]["income"]) * 0,30
        return quota > committed_income

    def _score_validation(self,data):
        return int(data["transaction"]["score"]) < 200 
    
    def _installments_validation(self,data):
        return int(data["transaction"]["installments"]) < 6


