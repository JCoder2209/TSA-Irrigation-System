import pandas as pd

def clean_and_prepare_data():
    input_file = "Crop_recommendationV2.csv"
    try:
        df = pd.read_csv(input_file)
    except:
        print("file wasn't found")
        return

    # had more columns, but we kept these; seemed most important
    cols_to_keep = []
    cols_to_keep.append('soil_moisture')
    cols_to_keep.append('temperature')
    cols_to_keep.append('humidity')
    cols_to_keep.append('rainfall')
    cols_to_keep.append('irrigation_frequency')

    # before finalizing, getting rid of the columns we don't need
    temporary_data = df[cols_to_keep]
    cleaned_data = temporary_data.dropna()

    cleaned_data = cleaned_data.rename(columns={
        'irrigation_frequency': 'water_needed'
    })

    cleaned_data.to_csv("soil_data.csv", index=False)
    print("Cleaned data saved to soil_data.csv")
