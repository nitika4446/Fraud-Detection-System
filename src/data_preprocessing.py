import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess(df):

    df = df.copy()

    cat_cols = ["Transaction_Type","Device","Location"]

    for col in cat_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

    return df