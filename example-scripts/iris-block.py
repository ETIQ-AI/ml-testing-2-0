from sklearn import datasets
import sklearn.model_selection
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
iris_df['target'] = iris.target
iris_train_df, iris_test_df = sklearn.model_selection.train_test_split(iris_df, test_size=0.2)
amodel = RandomForestClassifier(random_state=0)
iris_training_features = iris_train_df[iris.feature_names].copy()
iris_test_features = iris_test_df[iris.feature_names].copy()
iris_target_training = iris_train_df['target'].copy()
amodel.fit(iris_training_features, iris_target_training)
iris_target_testing = iris_test_df['target'].copy()
preds = amodel.predict(iris_test_features)
print(preds)