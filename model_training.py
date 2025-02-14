import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def build_irrigation_model():
    """
    Builds and trains a basic irrigation prediction model
    Using linear regression since it's easy to interpret
    """
    data_file = "soil_data.csv"
    farm_data = pd.read_csv(data_file) # Load the dataset
    features = ['soil_moisture', 'temperature', 'humidity', 'rainfall'] # our target variables
    target = 'water_needed'  # since we're trying to predict the water needed

    x = farm_data[features]
    y = farm_data[target]

    # Splitting data into training & test sets (80-20 split seems reasonable)
    print("Splitting data into training and test sets:")
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # initializing our model
    model = LinearRegression()
    model.fit(x_train, y_train)

    # evaluate the model's performance
    predictions = model.predict(x_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Model performance: Mean Squared Error = {mse:.3f}")
    model_filename = "irrigation_model.pkl" # saving our trained model
    joblib.dump(model, model_filename)
    print(f"Model saved as '{model_filename}'")
