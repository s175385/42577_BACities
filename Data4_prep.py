import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

df4 = pd.read_excel('Cities.xls', 'Sheet1')
for col in df4.columns:
    print(col)
df4 = df4.set_index("cityID")
df4 = df4.sort_index()
df4 = df4[["Car Modeshare (%)", "Public Transit Modeshare (%)", "Bicycle Modeshare (%)", "Walking Modeshare (%)",
         "Gasoline Pump Price (USD/liter)", "Road Deaths Rate (per 1000)", "Population", "Land Area (sq. km)",
         "Population Density (per sq. km)", "Population Change 1990 – 2000", "Population Change 2000 – 2010",
         "Population Change 2010 – 2020", "Population Change 2020 – 2025", "Urbanization Rate 2015 (%)",
         "Urbanization Rate Change 2015 – 2025 (pp)", "Sustainability Factor", "Population Factor"]]
df4.columns = df4.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('%', 'p').str.replace('–_', '').str.replace('.', '').str.replace('/', '')
print(df4.head())
print(df4.describe())
df4 = df4.replace(r'^\s*$', np.nan, regex=True)

#count = df4["car_modeshare_p"].isna().sum()
#print(count)

for column in df4:
    print(df4[column].isna().sum())

print(len(df4))
#drop all columns with more than 20 NaNs
df4 = df4.dropna(axis=1, thresh=311) #thresh = Require that many non-NaN values

print(df4.head())
print(df4.corr())
print("Mean: ")
print(df4.mean())
#fill the remaining NaNs with the columns mean
df4 = df4.fillna(df4.mean())
print(df4.head())

for col in df4.columns:
    print(col)
print("\n")
scaler = StandardScaler()
scaled_df4 = scaler.fit_transform(df4)
scaled_df4 = pd.DataFrame(scaled_df4, columns= ("gasoline_pump_price_usdliter", "road_deaths_rate_per_1000", "population", "land_area_sq_km", "population_density_per_sq_km", "population_change_1990_2000", "population_change_2000_2010", "population_change_2010_2020", "population_change_2020_2025", "urbanization_rate_2015_p", "urbanization_rate_change_2015_2025_pp", "sustainability_factor", "population_factor"))
print(scaler.fit(df4))
print(scaler.mean_)
print(scaler.transform(df4))
print(scaled_df4.head())

#plt.hist(df4.population_factor)
#plt.show()



