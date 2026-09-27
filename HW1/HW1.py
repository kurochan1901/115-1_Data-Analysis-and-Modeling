import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read dataset
df = pd.read_csv("taxi_trip_pricing.csv")

# Display first 5 rows
df.head()