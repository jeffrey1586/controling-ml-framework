"""
use --> node_paths = model.tree_.children_left
all the positive numbers are rule nodes. So append them to the correct rule
in inference_rules --> make dict
"""
from dataclasses import dataclass

@dataclass
class rule_dict:
    rules: dict
    node: int
    male: dict
    female: dict

def insertRuleProb(exp_prob, rule_dict, padding):
    male_node = 0
    female_node = 0
    node = rule_dict.node
    if rule_dict.node + padding in rule_dict.male:
        male_node = rule_dict.male[rule_dict.node + padding]
    if rule_dict.node + padding in rule_dict.female:
        female_node = rule_dict.female[rule_dict.node + padding]
    if padding == 0:
        tmp = {"rule": rule_dict.rules[0],
                            "node": rule_dict.node + padding,
                            "male": male_node,
                            "female": female_node}
        # exp_prob[0].append(tmp)
        print("ALMOST:", tmp)
    else:
        exp_prob[rule_dict.node] = {"rule": rule_dict.rules[rule_dict.node],
                                    "node": rule_dict.node + padding,
                                    "male": male_node,
                                    "female": female_node}
    return exp_prob

def countNodePassed(node, tmp):
    count = 0
    back = False
    for i in tmp:
        if tmp[i] == node:
            count += 1
    if count == 2:
        back = True
    return back

# Parsing extracted rules to ASP program
def ruleParser(model, rules, prob_male, prob_female):
    rule_dict.rules = rules
    rule_dict.node = 0
    rule_dict.male = prob_male
    rule_dict.female = prob_female
    exp_prob = {}
    tmp = []
    tree = model.tree_
    right = True
    left = True
    # exp_refute_prob = {0:""}
    max_node = sorted(list(rules))[-1]
    while rule_dict.node + 1 < max_node:
        if tree.children_left[rule_dict.node] and left:
            if countNodePassed(rule_dict.node, tmp):
                rule_dict.node -= 1
                left = False
                right = True
                continue
            tmp.append(rule_dict.node)
            print("node:", rule_dict.node)
            print("Left", tree.children_left[rule_dict.node])
            rule_dict.node += 1
            if tree.children_left[rule_dict.node] == -1:
                rule_dict.node -= 1
                tmp.append(rule_dict.node)
                left = False
                right = True
        elif tree.children_right[rule_dict.node] and right:
            print("node:", rule_dict.node)
            print("Right", tree.children_right[rule_dict.node])
            left = True
            right = False
            rule_dict.node = tree.children_right[rule_dict.node]

        # if rule_dict.node == 0 and "class" not in rule_dict.rules[1]:
        #     exp_prob = insertRuleProb(exp_prob, rule_dict, 1)
        # elif "class" in rule_dict.rules[rule_dict.node] and "class" in rule_dict.rules[rule_dict.node+1]:
        #     rule_dict.node += 1
        #     exp_prob = insertRuleProb(exp_prob, rule_dict, 0)
        #     print("rule!!:", rule_dict.rules[rule_dict.node])
        #     print("m/f!!:", rule_dict.male, rule_dict.female)
        #     print("hello", model.tree_.children_left[0])
        #     print("hello", model.tree_.children_right[0])
        #     continue
        # # if "class" in rule_dict.rules[rule_dict.node] and "class" in rule_dict.rules[rule_dict.node-1]:
        # #     exp_prob = insertRuleProb(exp_prob, rule_dict, 0)
        # #     rule_dict.node += 1
        # #     print("rule!!:", rule_dict.rules[rule_dict.node])
        # #     print("m/f!!:", rule_dict.male, rule_dict.female)
        # elif "class: 1" in rule_dict.rules[rule_dict.node + 1]:
        #     exp_prob = insertRuleProb(exp_prob, rule_dict, 2)
        # elif "class: 0" in rule_dict.rules[rule_dict.node + 1]:
        #     exp_prob = insertRuleProb(exp_prob, rule_dict, 1)
        # rule_dict.node += 1

    print("Rules:", rules)
    print("prob_male", prob_male)
    print("prob_female", prob_female)
    print("Prob dict:", exp_prob)
    return exp_prob
