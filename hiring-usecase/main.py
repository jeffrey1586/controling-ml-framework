"""

"""
from decisiontree import createDT
from rule_extractor import extractRules
from probabilities import getProbabilities
from rule_parser import ruleParser


model, X, X_train, data, dot_data = createDT(60,40)
print(data)
prob_male, prob_female = getProbabilities(model, X, X_train, data)
node_rules = extractRules(model, X, dot_data)
exp_with_prob = ruleParser(model, node_rules, prob_male, prob_female)

# print("Male prob:", prob_male)
# print("Female prob:", prob_female)
# print("Rules:", rules)
