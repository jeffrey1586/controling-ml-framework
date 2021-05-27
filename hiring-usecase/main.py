"""

"""

from decisiontree import createDT
from rule_extractor import extractRules
from probabilities import getProbabilities


model, X, X_train, data = createDT(60,40)
prob_male, prob_female = getProbabilities(model, X, X_train, data)
rules = extractRules(model, X)
