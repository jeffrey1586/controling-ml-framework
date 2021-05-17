from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from IPython.display import Image
import pydotplus
import pandas as pd
import numpy as np
import random

# Load data
iris = load_iris()
X = iris.get('data')
y = iris.get('target')

# Create decision tree classifer object
clf = DecisionTreeClassifier(random_state=0)

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
model = clf.fit(X_train, y_train)

# Create DOT data
dot_data = tree.export_graphviz(clf, out_file=None,feature_names=iris.feature_names,
                                class_names=iris.target_names)

# Draw graph
graph = pydotplus.graph_from_dot_data(dot_data)

## Color of nodes
# nodes = graph.get_node_list()
#
# for node in nodes:
#     if node.get_label():
#         values = [int(ii) for ii in node.get_label().split('value = [')[1].split(']')[0].split(',')];
#         color = {0: [255,255,224], 1: [255,224,255], 2: [224,255,255],}
#         values = color[values.index(max(values))]; # print(values)
#         color = '#{:02x}{:02x}{:02x}'.format(values[0], values[1], values[2]); # print(color)
#         node.set_fillcolor(color )

# Create PNG
Image(graph.create_png() )
graph.write_png("iris3.png")
