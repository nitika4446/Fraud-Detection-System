import joblib

from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

def train_models(X_train,y_train):

    rf = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    rf.fit(X_train,y_train)

    xgb = XGBClassifier()

    xgb.fit(X_train,y_train)

    joblib.dump(rf,"models/random_forest.pkl")
    joblib.dump(xgb,"models/xgboost_model.pkl")

    return rf,xgb