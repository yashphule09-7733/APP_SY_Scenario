# Hotel Room Rent Analysis System

import numpy as np
import pandas as pd

# Step 1: Create NumPy array of room rents
rent = np.array([2500, 3500, 4500, 5000, 3000, 6000, 4000, 5500])

# Step 2: Calculate statistical values
print("Room Rents:", rent)

print("Mean Room Rent:", np.mean(rent))
print("Median Room Rent:", np.median(rent))
print("Maximum Room Rent:", np.max(rent))
print("Minimum Room Rent:", np.min(rent))

# Step 3: Create hotel room records
data = {
    'Room No': [101, 102, 103, 104, 105, 106, 107, 108],
    'Room Rent': rent
}

# Step 4: Create Pandas DataFrame
df = pd.DataFrame(data)

print("\nHotel Room Records:")
print(df)

# Step 5: Display rooms having rent greater than 4000
print("\nRooms Having Rent Greater Than 4000:")
print(df[df['Room Rent'] > 4000])
