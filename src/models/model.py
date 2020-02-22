import json
from src.utils.constants import CalculationValues
from src.utils.constants import Violations

class CreditTransactions():

    def __init__(self):
        self.constant = CalculationValues()
        self.violation = Violations()
    
    def transport_trasaction(self, data):
        data = json.loads(data)
        violations = [self._transport_transaction(data), self._income_validation(data), self._score_validation(data)]
        return {"id":data["transaction"]["id"], "violations":violations}

    def _income_validation(self,data):
        quota = int(data["transaction"]["requested_value"]) / int(data["transaction"]["installments"])
        committed_income = int(data["transaction"]["income"]) * self.constant.compromised_rate
        if (quota > committed_income):
            return self.violation.compromised-income

    def _score_validation(self,data):
        if (int(data["transaction"]["score"]) < self.constant.minimum_score):
            return self.violation.low_score  
    
    def _installments_validation(self,data):
        if (int(data["transaction"]["installments"]) < self.constant.minimum_installments)):
            return self.violation.minimum_installments

