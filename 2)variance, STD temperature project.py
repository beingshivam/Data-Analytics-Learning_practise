import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

#print(london_data.head())
#print(london_data.iloc[100:200])
#print(len(london_data))

temp = london_data["TemperatureC"]

average_temp = np.average(temp)
temperature_standard_deviation = np.std(temp)
temp_var = np.var(temp)
#print(temp_var)
#print(average_temp)
#print(temperature_standard_deviation)

#print(london_data.tail())

#filter by month column

june = london_data.loc[london_data["month"]==6]["TemperatureC"]

july = london_data.loc[london_data["month"]==7]["TemperatureC"]

avg_temp_june = np.average(june)
avg_temp_july = np.average(july)

print(avg_temp_june)
print(avg_temp_july)
print(np.std(june))
print(np.std(july))

#mean and STD for all months

for i in range(1,13):
  month_temp = london_data.loc[london_data['month']==i]['TemperatureC']
  print("Mean for "+str(i)+"month is->"+ str(np.average(month_temp)))
  print("STD for "+str(i)+"month is->"+ str(np.std(month_temp)))
  #temp_list = temp_list.add(month_temp)
  

#pressure = london_data.loc[london_data["PressurehPa"]]['TemperatureC']
#print(pressure)
  



