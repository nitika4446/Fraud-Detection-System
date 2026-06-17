from sklearn.metrics import accuracy_score

def evaluate(model,X_test,y_test):

    pred = model.predict(X_test)

    score = accuracy_score(y_test,pred)

    return score