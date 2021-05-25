"""

"""

from decisiontree import createDT
from rule_extractor import extractRules
from probabilities import getProbabilities

model, X, data = createDT(80,20)
probabilities = getProbabilities(model, X, data)
rules = extractRules(model, X)
