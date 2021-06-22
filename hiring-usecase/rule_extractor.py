"""
Two functions in this file are derived from:
https://github.com/scikit-learn/scikit-learn/blob/15a949460/sklearn/tree/_export.py#L665
The functions _add_leaf() and print_tree_recurse() are derived from the tree export
module from scikit-learn. These are however modified.

Besides that new functions are added in order to extract the correct information
to parse it to an asp program.

returns all rules in DT as report format (String)
"""

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn.tree import _tree
from dataset import createDataset
import numpy as np

export_text.report = "" # Default

def _add_leaf(model, value_fmt, value, class_name, indent):
    decimals = 2 # Default
    show_weights = False # Default
    val = ''
    is_classification = isinstance(model, DecisionTreeClassifier)
    if show_weights or not is_classification:
        val = ["{1:.{0}f}, ".format(decimals, v) for v in value]
        val = '['+''.join(val)[:-2]+']'
    if is_classification:
        val += ' class: ' + str(class_name)
    export_text.report += value_fmt.format(indent, '', val)

def print_tree_recurse(model, X, node, depth):
    decimals = 2 # Default
    max_depth = 10 # Default
    right_child_fmt = "{} {} <= {}\n" # Default
    left_child_fmt = "{} {} >  {}\n" # Default
    truncation_fmt = "{} {}\n" # Default
    show_weights = False # Default
    if isinstance(model, DecisionTreeClassifier):
        value_fmt = "{}{} weights: {}\n"
        if not show_weights:
            value_fmt = "{}{}{}\n"
    else:
        value_fmt = "{}{} value: {}\n"

    tree_ = model.tree_
    class_names = model.classes_
    feature_names_ = [X.columns[i] if i != _tree.TREE_UNDEFINED
                                else None for i in tree_.feature]

    indent = ""
    value = None
    if tree_.n_outputs == 1:
        value = tree_.value[node][0]
    else:
        value = tree_.value[node].T[0]
    class_name = np.argmax(value)

    if (tree_.n_classes[0] != 1 and
            tree_.n_outputs == 1):
        class_name = class_names[class_name]

    if depth <= max_depth+1:
        info_fmt = ""
        info_fmt_left = info_fmt
        info_fmt_right = info_fmt

        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_names_[node]
            threshold = tree_.threshold[node]
            threshold = "{1:.{0}f}".format(decimals, threshold)
            export_text.report += right_child_fmt.format(indent,
                                                         name,
                                                         threshold)
            export_text.report += info_fmt_left
            print_tree_recurse(model, X, tree_.children_left[node], depth+1)

            export_text.report += left_child_fmt.format(indent,
                                                        name,
                                                        threshold)
            export_text.report += info_fmt_right
            print_tree_recurse(model, X, tree_.children_right[node], depth+1)
        else:  # leaf
            _add_leaf(model, value_fmt, value, class_name, indent)
    else:
        subtree_depth = _compute_depth(tree_, node)
        if subtree_depth == 1:
            _add_leaf(model, value_fmt, value, class_name, indent)
        else:
            trunc_report = 'truncated branch of depth %d' % subtree_depth
            export_text.report += truncation_fmt.format(indent,
                                                        trunc_report)

# insert the rules of each node in a dictionary
def sumRules(all_nodes):
    rule_dict = {1:""}
    current = 1
    for i in all_nodes:
        if i != "\n":
            rule_dict[current] = rule_dict[current] + i
        else:
            current += 1
            rule_dict[current] = ""
    if rule_dict[current] == "":
        del rule_dict[current]
    # print("All nodes: ",rule_dict) #show all nodes untransformed
    return rule_dict

# transform the rule expression according to the inference path
def transRules(all_nodes, model, dot_data):
    rule_dict = sumRules(all_nodes)
    for key, value in list(rule_dict.items()):
        if ">" in value:
            del rule_dict[key]
    node = 0
    for key in list(rule_dict.keys()):
        rule_dict[node] = rule_dict.pop(key)
        node += 1
    for key, value in list(rule_dict.items()):
        if key+1 in rule_dict and rule_dict[key+1] == ' class: 1':
            rule_dict[key] = value.replace('<=', '>')
    # print('Rules per node: ', rule_dict) #show all nodes transformed
    return rule_dict

# Extract the rules from the DT/model
def extractRules(model, X, dot_data):
    print_tree_recurse(model, X, 0, 1)
    all_nodes = export_text.report
    node_rules = transRules(all_nodes, model, dot_data)
    return node_rules
