"""
The createDatabase function is able to generate a database of candidates.
"""
# install guide
# sudo pip3 install names
# sudo pip3 install Faker
# sudo pip3 install pandas
# sudo pip3 install numpy

# Import packages
from random import shuffle, seed
from faker.providers.person.en import Provider
import pandas as pd
import numpy as np
import random

# Create list of 100 unique random names
def createNames(nmr_male, nmr_female):
    first_names_male = list(set(Provider.first_names_male))
    seed(4321)
    shuffle(first_names_male)
    names = first_names_male[0:nmr_male]

    first_names_female = list(set(Provider.first_names_female))
    seed(4321)
    shuffle(first_names_female)
    names.extend(first_names_female[0:nmr_female])
    return names

# Create list of gender according to generated names
# 0 = male and 1 = female
def createGender(nmr_male,nmr_female):
    gender = []
    while len(gender) != nmr_male:
        gender.append(0)

    while len(gender)-nmr_male != nmr_female:
        gender.append(1)
    return gender

# Create list of random ratings
def createRating(candidates):
    ratings = []
    while len(ratings) != candidates:
        rate = round(np.random.gamma(9, 0.5)) #gamma distributed, normal around the 5
        if rate > 10:
            rate = 10
        ratings.append(rate)
    return ratings

# Create list of random education
# 0 = highschool, 1 = bachelor and 2 = master
def createEdu(candidates):
    education_types = [0,1,2]
    education = []
    while len(education) != candidates:
        education.append(random.choice(education_types))
    return education

# Create list of random workyears
def createWork(candidates):
    workyears = []
    while len(workyears) != candidates:
        workyears.append(round(np.random.gamma(1, 2.0))) # gamma distributed
    return workyears

# Create list of random levels in programming skill
# 0 = low, 1 = moderate, 2 = advanced
def createProgram(candidates):
    programming_level = [0,1,2]
    programming = []
    while len(programming) != candidates:
        programming.append(random.choice(programming_level))
    return programming

# Create column indicating if the candidate (row) is hired or not, according
# to the main inference
# 0 = hired, 1 = not hired
def hiring(data):
    hiring = []
    for index, row in data.iterrows():
        rating = row.biorating
        education = row.education
        workyears = row.workyears
        programming = row.programming
        # Main infererence
        if (rating > 5 and education != 0 and workyears >=3 and
        programming != 0):
            hiring.append(0)
        else:
            hiring.append(1)
    return hiring

# Generate database
def createDataset(nmr_male,nmr_female):
    names = createNames(nmr_male,nmr_female)
    data = pd.DataFrame(names, columns=['name'])
    data['gender'] = createGender(nmr_male,nmr_female)
    data['biorating'] = createRating(len(names))
    data['education'] = createEdu(len(names))
    data['workyears'] = createWork(len(names))
    data['programming'] = createProgram(len(names))
    data['hire'] = hiring(data)
    return data
