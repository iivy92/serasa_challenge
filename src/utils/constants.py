from enum import Enum 

class CalculationValues(Enum):
    minimum_score = 200
    minimum_installments = 3
    compromised_rate = 0.3

class Violations(Enum):
    compromised_income = "compromised-income"
    low_score = "low-score"
    minimum_installments = "minimum-installments"
    doubled_transactions = "doubled-transactions"