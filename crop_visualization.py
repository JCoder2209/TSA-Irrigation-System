import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_irrigation_trends(readings):
    """
    Shows how water needs change with soil moisture, and adds adequate styling
    """
    plot_data = pd.DataFrame(readings,columns=["Soil Moisture", "Predicted Water Needed"])
    plt.figure(figsize=(10, 5)) # best for windows
    sns.lineplot(data=plot_data, x="Soil Moisture", y="Predicted Water Needed", marker="o") # circles are best for visuals

    plt.xlabel("% Soil Moisture")
    plt.ylabel("# Water Liters needed")
    plt.title("Amount of water needed from soil moisture")
    plt.grid(True, alpha=0.35)  # making grid look best with 0.3-0.35
    plt.show()

def show_training_data_distribution():
    """
    Shows the distribution of our training data.
    needed for spotting unusual patterns or outliers
    """
    training_data = pd.read_csv("soil_data.csv")
    # create subplots for each feature
    plt.figure(figsize=(10, 6))
    training_data.hist(bins=20, figsize=(10, 6))
    plt.suptitle("Distribution of our training data")
    plt.tight_layout() # needed to prevent overlap
    plt.show()