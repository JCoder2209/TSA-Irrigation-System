import data_preprocessing as dp  # handles all the messy data stuff
import model_training as mt
import agri_utils as au  # our utility functions
import numpy as np
import pandas as pd
import os
import crop_visualization as cz  # visualization stuff we added later

dp.clean_and_prepare_data() # clean
# checking if we need to train the model
model_file = "irrigation_model.pkl"
if not os.path.exists(model_file):
    print("No existing model found, training one now;")
    mt.build_irrigation_model()
else:
    print("model already trained")

# generate the test predictions
moisture_readings = []
features = ['soil_moisture', 'temperature', 'humidity', 'rainfall']

# simulate 20 different moisture scenarios
for i in range(20):
    # random moisture between 10-60 (based on past research)
    curr_moisture = np.random.uniform(10, 60)

    # keeping the temp and humidity constant for now
    test_data = pd.DataFrame([[curr_moisture, 25, 60, 5]], columns=features)
    water_needed = au.estimate_water_requirement(test_data)
    moisture_readings.append((curr_moisture, water_needed))

# Finally, visualize results
cz.plot_irrigation_trends(moisture_readings)
cz.show_training_data_distribution()