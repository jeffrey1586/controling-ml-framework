"""

"""

from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from dataset import createDataset
import pydotplus
# from IPython.display import Image

# Load data
data = createDataset(70,70) #arg1= nmr_male and arg2 = nmr_female
X = data.loc[:, 'gender':'programming']
y = data.loc[:, 'hire']
print(data.loc[data['hire'] == 0]) #show which row(s) are hired candidates

# Create decision tree classifer
clf = DecisionTreeClassifier(random_state=0)

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
model = clf.fit(X_train, y_train)

# Create DOT data for the decision tree
dot_data = tree.export_graphviz(model, out_file=None,feature_names=list(X.columns),
                                class_names=True)

# Draw the graph
graph = pydotplus.graph_from_dot_data(dot_data)

# Create PNG and save in current folder
# Image(graph.create_png())
graph.write_png("decision_tree.png")