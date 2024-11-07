import os
print(os.getcwd())

import pandas as pd
tres_data = pd.read_csv(r'c:\Users\LENOVO\Downloads\trestle_academy_dataset.csv')
print(tres_data)

#identifying and handling missing values
missing_values = tres_data.isnull().sum()
print(missing_values)

#standardizing text data
tres_data['enrollment_date'] = pd.to_datetime(tres_data['enrollment_date'], errors='coerce')
print(tres_data.dtypes)

#normalizing text data
tres_data['course'] = tres_data['course'].str.title()
print(tres_data['course'].unique())

#filtering unwanted data
filtered_tres_data = tres_data[(tres_data['age'] >= 18) & (tres_data['age'] <= 45)]
original_count = tres_data.shape[0]
filtered_count = filtered_tres_data.shape[0]
print("Original row count:", original_count)
print("Filtered row count:", filtered_count)

#correcting inconsistent entries
tres_data['is_intern'] = tres_data['is_intern'].str.title()
print(tres_data['is_intern'].unique())