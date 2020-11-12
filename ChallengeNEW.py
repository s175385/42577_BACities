import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

df = pd.read_excel('Cities.xls', 'Sheet1')
for col in df.columns:
    print(col)
df = df.set_index("cityID")
df = df.sort_index()
df = df[["Car Modeshare (%)", "Public Transit Modeshare (%)", "Bicycle Modeshare (%)", "Walking Modeshare (%)",
         "Gasoline Pump Price (USD/liter)", "Road Deaths Rate (per 1000)", "Population", "Land Area (sq. km)",
         "Population Density (per sq. km)", "Population Change 1990 – 2000", "Population Change 2000 – 2010",
         "Population Change 2010 – 2020", "Population Change 2020 – 2025", "Urbanization Rate 2015 (%)",
         "Urbanization Rate Change 2015 – 2025 (pp)", "Sustainability Factor", "Population Factor"]]
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('%', 'p').str.replace('–_', '').str.replace('.', '').str.replace('/', '')
print(df.head())
print(df.describe())
df = df.replace(r'^\s*$', np.nan, regex=True)

#count = df["car_modeshare_p"].isna().sum()
#print(count)

for column in df:
    print(df[column].isna().sum())

print(len(df))
#drop all columns with more than 20 NaNs
df = df.dropna(axis=1, thresh=311) #thresh = Require that many non-NaN values

print(df.head())
print(df.corr())
print("Mean: ")
print(df.mean())
#fill the remaining NaNs with the columns mean
df = df.fillna(df.mean())
print(df.head())

for col in df.columns:
    print(col)
print("\n")
scaler = StandardScaler()
scaled_df = scaler.fit_transform(df)
scaled_df = pd.DataFrame(scaled_df, columns= ("gasoline_pump_price_usdliter", "road_deaths_rate_per_1000", "population", "land_area_sq_km", "population_density_per_sq_km", "population_change_1990_2000", "population_change_2000_2010", "population_change_2010_2020", "population_change_2020_2025", "urbanization_rate_2015_p", "urbanization_rate_change_2015_2025_pp", "sustainability_factor", "population_factor"))
print(scaler.fit(df))
print(scaler.mean_)
print(scaler.transform(df))
print(scaled_df.head())

plt.hist(df.population_factor)
#plt.show()



