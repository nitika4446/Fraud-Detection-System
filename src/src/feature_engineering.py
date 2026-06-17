def create_features(df):

    df["Amount_Per_Age"] = df["Amount"] / (df["Age"] + 1)

    return df