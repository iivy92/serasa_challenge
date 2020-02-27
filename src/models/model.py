import json
import os
from datetime import datetime, timedelta
from src.utils.constants import CalculationValues
from src.utils.constants import Violations
from src.settings.system import SystemSettings

class CreditTransactions():

    def __init__(self):
        self.settings = SystemSettings()
    #     self._income_validation()
    #     self._score_validation()
    #     self._installments_validation()
    
    def transport_trasaction(self, data):
        analysis = [self._income_validation(data), self._score_validation(data), self._installments_validation(data), self._double_transaction_validation(data)] 
        violations=[]
        for analyze in analysis:
            if analyze:
                violations.append(analyze)
            
        return {"id":data["transaction"]["id"], "violations": violations}
    
    def save_transaction(self, data_file):       
        temp = []
        loads = self._read_transaction_file()
        if loads:
            for load in loads:
                temp.append(load)

        temp.append(data_file)
        temp.sort(key = lambda x: datetime.strptime(x["transaction"]["time"], '%Y-%m-%dT%H:%M:%S.%f%z'), reverse=True)
        import ipdb; ipdb.set_trace()
        self._save_transaction_file(temp)       

    def _income_validation(self,data):
        quota = int(data["transaction"]["requested_value"]) / int(data["transaction"]["installments"])
        committed_income = int(data["transaction"]["income"]) * CalculationValues.compromised_rate.value
        if (quota > committed_income):
            return Violations.compromised_income.value

    def _score_validation(self,data):
        if (int(data["transaction"]["score"]) < CalculationValues.minimum_score.value):
            return Violations.low_score.value 
    
    def _installments_validation(self,data):
        if (int(data["transaction"]["installments"]) < CalculationValues.minimum_installments.value):
            return Violations.minimum_installments.value
    
    def _double_transaction_validation(self,data):
        loads = self._read_transaction_file()
        
        if loads:        
            for load in loads:
                if (data["transaction"]["id"] == load["transaction"]["id"]):
                    diff = datetime.strptime(data["transaction"]["time"], '%Y-%m-%dT%H:%M:%S.%f%z') - datetime.strptime(load["transaction"]["time"], '%Y-%m-%dT%H:%M:%S.%f%z')
                    if diff <= timedelta(seconds=CalculationValues.minimum_time.value):
                        return Violations.doubled_transactions.value

    def _read_transaction_file(self):
        if os.path.exists(str(self.settings.PATH_TRANSACTIONS)):
            with open (str(self.settings.PATH_TRANSACTIONS), "r") as output_file:
                json_data = json.loads(output_file.read())
            
            return json_data  

    def _save_transaction_file(self, data):
        with open (str(self.settings.PATH_TRANSACTIONS), "w") as output_file:
            json.dump(data, output_file, indent=4)      

credit_transactions = CreditTransactions()