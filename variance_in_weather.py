import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data


# print(london_data.head())
#print(london_data.iloc[100:200])
print(len(london_data))

temp = london_data["TemperatureC"]
#print(temp.head())
average_temp = np.mean(temp)
print(average_temp)
temperature_var = np.var(temp)
print(temperature_var)
temperature_standard_deviation = np.std(temp)
print(temperature_standard_deviation)

#print(london_data.head())
#print(london_data.tail())

june = london_data.loc[london_data["month"] == 6]["TemperatureC"]
#print(june.head())
july = london_data.loc[london_data["month"] == 7]["TemperatureC"]
#print(july.head())

june_mean_temp = np.mean(june)
print(june_mean_temp)
july_mean_temp = np.mean(july)
print(july_mean_temp)

june_std_temp = np.std(june)
print(june_std_temp)
july_std_temp = np.std(july)
print(july_std_temp)

# temperature
# for i in range(1, 13):
#   month = london_data.loc[london_data["month"] == i]["TemperatureC"]
#   print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
#   print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")

# humidity
# for i in range(1, 13):
#   month = london_data.loc[london_data["month"] == i]["Humidity"]
#   print("The mean humidity in month "+str(i) +" is "+ str(np.mean(month)))
#   print("The standard deviation of humidity in month "+str(i) +" is "+ str(np.std(month)) +"\n")

# print(london_data.tail())
# hour
for i in range(1, 23+1):
  hour = london_data.loc[london_data["hour"] == i]["TemperatureC"]
  print("The mean temperature in hour "+str(i) +" is "+ str(np.mean(hour)))
  print("The standard deviation of Temperature in hour "+str(i) +" is "+ str(np.std(hour)) +"\n")
