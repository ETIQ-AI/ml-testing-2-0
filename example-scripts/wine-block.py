from sklearn import datasets
import sklearn.model_selection
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
wine = datasets.load_wine()
wine_df = pd.DataFrame(wine.data, columns=wine.feature_names)
wine_df['target'] = wine.target
wine_train_df, wine_test_df = sklearn.model_selection.train_test_split(wine_df, test_size=0.2)
amodel = RandomForestClassifier(random_state=0)
wine_training_features = wine_train_df[wine.feature_names].copy()
wine_test_features = wine_test_df[wine.feature_names].copy()
wine_target_training = wine_train_df['target'].copy()
amodel.fit(wine_training_features, wine_target_training)
wine_target_testing = wine_test_df['target'].copy()
preds = amodel.predict(wine_test_features)
