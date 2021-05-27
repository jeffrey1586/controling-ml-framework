"""
returns two dictionaries (one for male and one for female) with the nodes as keys
and the corresponding probability of the gender for that node as value
"""
import pandas as pd

#
def insert2Dict(path, dict, row):
    for node in path:
        if node not in dict:
            dict[node] = 0
        dict[node] = dict[node] + 1
    return dict

#
def sumDict(male_dict, female_dict):
    sum_dict = {0:0}
    for key in male_dict:
        if key not in sum_dict:
            sum_dict[key] = 0
        sum_dict[key] += male_dict[key]
    for key in female_dict:
        if key not in sum_dict:
            sum_dict[key] = 0
        sum_dict[key] += female_dict[key]
    return sum_dict

#
def probCalculator(sum_dict, male_dict, female_dict, prob_male, prob_female, key, spacing):
    if key in male_dict:
        prob_male[key] = male_dict[key] / sum_dict[key-spacing]
    if key in female_dict:
        prob_female[key] = female_dict[key] / sum_dict[key-spacing]
    return prob_male, prob_female

#
def calcProbabilities(sum_dict, male_dict, female_dict, model):
    prob_male = {0:0}
    prob_female = {0:0}
    paths = model.tree_.children_left
    print(paths)
    print(sum_dict)
    for key in sum_dict:
        if key == 0:
            continue
        elif paths[key] != -1 and paths[key-1] == -1 and paths[key-2] == -1:
            prob_male, prob_female = probCalculator(sum_dict, male_dict,
                                                    female_dict, prob_male,
                                                    prob_female, key, key)
        elif paths[key] == -1 and paths[key-1] != -1:
            prob_male, prob_female = probCalculator(sum_dict, male_dict,
                                                    female_dict, prob_male,
                                                    prob_female, key, 1)
        elif paths[key] != -1 and paths[key-1] == -1:
            prob_male, prob_female = probCalculator(sum_dict, male_dict,
                                                    female_dict, prob_male,
                                                    prob_female, key, 2)
        elif paths[key-1] != -1:
            prob_male, prob_female = probCalculator(sum_dict, male_dict,
                                                    female_dict, prob_male,
                                                    prob_female, key, 1)
        elif paths[key] == -1 and paths[key-1] == -1:
            prob_male, prob_female = probCalculator(sum_dict, male_dict,
                                                    female_dict, prob_male,
                                                    prob_female, key, 2)
    return prob_male, prob_female

#
def setProbabilities(male_dict, female_dict, model):
    sum_dict = sumDict(male_dict, female_dict)
    probabilities = calcProbabilities(sum_dict, male_dict, female_dict, model)
    return probabilities

#
def getProbabilities(model, X, X_train, data):
    male_dict = {0:0}
    female_dict = {0:0}
    paths = model.decision_path(X).tolil()
    array_paths = paths.rows
    for index, row in X_train.iterrows():
        if row.gender == 0: #male
            male_dict = insert2Dict(array_paths[row.name], male_dict, row)
        elif row.gender == 1: #female
            female_dict = insert2Dict(array_paths[row.name], female_dict, row)
    prob_male, prob_female = setProbabilities(male_dict, female_dict, model)
    # print("male", male_dict)
    # print("female", female_dict)
    # print("prob male:", prob_male)
    # print("prob female:", prob_female)
    return prob_male, prob_female #probabilities
