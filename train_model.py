import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

FEATURES = [
    "age",
    "studytime",
    "failures",
    "absences",
    "G1",
    "G2",
]

MODEL_PATH = "model.pkl"


def load_data():
    return pd.read_csv("student_data.csv")


def train_model(df):
    X = df[FEATURES]
    y = df["G3"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)

    return model, mae


def main():
    df = load_data()

    model, mae = train_model(df)

    print(f"Model trained successfully")
    print(f"Mean Absolute Error: {mae:.2f}")

    joblib.dump(model, MODEL_PATH)
    print(f"Model saved as {MODEL_PATH}")


if __name__ == "__main__":
    main()