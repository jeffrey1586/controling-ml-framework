"""

"""
import pandas as pd

def getProbabilities(model, X, data):
    male_dict = {0:0}
    female_dict = {0:0}
    paths = model.decision_path(X).tolil()
    count = 0
    for path in paths.rows:
        # i = Person
        if data.iloc[count].gender == 0: #male
            for node in path:
                if node not in male_dict:
                    male_dict[node] = 0
                male_dict[node] = male_dict[node] + 1
        elif data.iloc[count].gender == 1: #female
            for node in path:
                if node not in female_dict:
                    female_dict[node] = 0
                female_dict[node] = female_dict[node] + 1
        count += 1
    print("male", male_dict)
    print("female", female_dict)
    return
